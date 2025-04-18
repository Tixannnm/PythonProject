import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime

conn = sqlite3.connect('weather.sl3')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather (
        date_time TEXT,
        temperature REAL
    )
''')
conn.commit()


url = 'https://sinoptik.ua/'
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.RequestException as e:
    print("Помилка при отриманні даних:", e)
    conn.close()
    exit()


soup = BeautifulSoup(response.text, 'html.parser')


temp_elem = soup.find_all('p', class_='R1ENpvZz')
temp1 = temp_elem[0].text
temp = int(temp1[1:3])
print(temp)


# if temp_elem:
#     try:
#
#         temperature = float(temp_elem.text.strip().replace('°', ''))
#     except ValueError:
#         print("Не вдалося перетворити значення температури в число")
#         conn.close()
#         exit()
# else:
#     print("Елемент з температурою не знайдено на сторінці")
#     conn.close()
#     exit()


now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
cursor.execute('INSERT INTO weather (date_time, temperature) VALUES (?, ?)', (now, temp))
conn.commit()

print(f"Дані збережено. Час: {now}, Температура: {temp}°.")

conn.close()
