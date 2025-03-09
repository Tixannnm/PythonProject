import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.2
        self.gladness -= 5
        self.money -= 5  # Витрати на навчальні матеріали

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        if self.money >= 10:
            print("Rest time")
            self.gladness += 7
            self.progress -= 0.1
            self.money -= 10  # Витрати на відпочинок
        else:
            print("Not enough money to chill")
            self.to_work()

    def to_work(self):
        print("Time to work")
        self.money += 20
        self.gladness -= 4
        self.progress -= 0.05

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.money < 0:
            print("Bankrupt…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        print(f"{' Day ' + str(day) + ' of ' + self.name + ' life ':*^50}")
        if self.money < 20:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        elif self.gladness < 20:
            self.to_chill()
        else:
            choice = random.randint(1, 4)
            if choice == 1:
                self.to_study()
            elif choice == 2:
                self.to_sleep()
            elif choice == 3:
                self.to_chill()
            elif choice == 4:
                self.to_work()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
for day in range(365):
    if not nick.alive:
        break
    nick.live(day)