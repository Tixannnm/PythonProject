from bs4 import BeautifulSoup
import requests
response = requests.get("https://minfin.com.ua/ua/currency/mb/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all(class_="sc-1x32wa2-9 bKmKjX")
    # print(soup)
    res = soup_list[0]
    # print(type(res))
    # print(res.text)
    curs = res.text[0:6]
    curs = curs.replace(",", ".")
    curs2 = float(curs)
    print("Курс Доллор - ", curs)
    grn = float(input("Введіть кількість гривень: "))
    result = grn/curs2
    print("Ви отримаете: ", round(result, 2), "$")