import logging
import random

# Налаштовуємо логування
logging.basicConfig(filename='simulation_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()
        logging.info(f"{self.name} отримав будинок.")

    def get_car(self):
        self.car = Auto(brands_of_car)
        logging.info(f"{self.name} придбав автомобіль {self.car.brand}.")

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
        logging.info(f"{self.name} отримав роботу: {self.job.job} з зарплатою {self.job.salary}.")

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
        logging.info(f"{self.name} поїв. Ситість: {self.satiety}.")

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
        logging.info(f"{self.name} попрацював. Зараз гроші: {self.money}, радість: {self.gladness}, ситість: {self.satiety}.")

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            self.money -= 100
            self.car.fuel += 100
            logging.info(f"{self.name} купив паливо. Гроші: {self.money}, паливо в машині: {self.car.fuel}.")
        elif manage == "food":
            self.money -= 50
            self.home.food += 50
            logging.info(f"{self.name} купив їжу. Гроші: {self.money}, їжа вдома: {self.home.food}.")
        elif manage == "delicacies":
            self.gladness += 10
            self.satiety += 2
            self.money -= 15
            logging.info(f"{self.name} купив делікатеси. Гроші: {self.money}, ситість: {self.satiety}, радість: {self.gladness}.")

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        logging.info(f"{self.name} відпочивав. Радість: {self.gladness}, безлад у будинку: {self.home.mess}.")

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
        logging.info(f"{self.name} прибрав у будинку. Радість: {self.gladness}, безлад: {self.home.mess}.")

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
        logging.info(f"{self.name} відремонтував автомобіль. Гроші: {self.money}, міцність авто: {self.car.strength}.")

    def days_indexes(self, day):
        day = f" Сьогодні {day} день життя {self.name} "
        logging.info(f"{day:=^50}")
        logging.info(f"Гроші – {self.money}")
        logging.info(f"Ситість – {self.satiety}")
        logging.info(f"Радість – {self.gladness}")
        logging.info(f"Їжа – {self.home.food}")
        logging.info(f"Безлад – {self.home.mess}")
        logging.info(f"Паливо – {self.car.fuel}")
        logging.info(f"Міцність – {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            logging.warning(f"{self.name} впав в депресію.")
            return False
        if self.satiety < 0:
            logging.warning(f"{self.name} помер від голоду.")
            return False
        if self.money < -500:
            logging.warning(f"{self.name} банкрут.")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strength < 15:
            self.to_repair()
        elif dice == 1:
            self.chill()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.clean_home()
        elif dice == 4:
            self.shopping(manage="delicacies")


brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},
    "Lada":{"fuel":50, "strength":40, "consumption": 10},
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14} }

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            logging.warning(f"Автомобіль {self.brand} не може рухатись.")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
 "Java developer": {"salary":50, "gladness_less": 10},
 "Python developer": {"salary":40, "gladness_less": 3},
 "C++ developer": {"salary":45, "gladness_less": 25},
 "Rust developer": {"salary":70, "gladness_less": 1},
 }

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

nick = Human(name="Nick")
for day in range(1, 800):
    if nick.live(day) == False:
        break
