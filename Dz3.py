import random

class Pet:
    def __init__(self, name, happiness=50, hunger=50):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
    
    def play(self):
        self.happiness += 10
        self.hunger -= 5
        print(f"{self.name} грається та стає щасливішим!")
    
    def feed(self):
        self.hunger += 10
        print(f"{self.name} поїв і тепер ситий!")
    
    def status(self):
        print(f"{self.name}: Щастя {self.happiness}, Голод {self.hunger}")

class Human:
    def __init__(self, name="Human", pet=None):
        self.name = name
        self.money = 100
        self.pet = pet

    def interact_with_pet(self):
        if self.pet:
            action = random.choice(["play", "feed"])
            if action == "play":
                self.pet.play()
            else:
                self.pet.feed()
        else:
            print("У мене немає домашнього улюбленця!")

nick = Human(name="Nick", pet=Pet(name="Buddy"))
for day in range(1, 5):
    print(f"День {day}")
    nick.interact_with_pet()
    nick.pet.status()
    print("-")

# Друга симуляція
class Farm:
    def __init__(self):
        self.food = 100
        self.animals = 10
    
    def harvest(self):
        self.food += 50
        print("Зібрано урожай!")
    
    def feed_animals(self):
        if self.food >= 20:
            self.food -= 20
            print("Тварини нагодовані!")
        else:
            print("Немає достатньо їжі для тварин!")

class Farmer:
    def __init__(self, name, farm):
        self.name = name
        self.farm = farm
    
    def work(self):
        action = random.choice(["harvest", "feed"])
        if action == "harvest":
            self.farm.harvest()
        else:
            self.farm.feed_animals()

farm = Farm()
farmer = Farmer(name="John", farm=farm)

for day in range(1, 5):
    print(f"День {day}")
    farmer.work()
    print(f"На фермі їжі: {farm.food}")
    print("-")

# Додані нові рядки
print("Симуляція завершена!")
nick.pet.play()
nick.pet.feed()
farm.harvest()
farmer.work()