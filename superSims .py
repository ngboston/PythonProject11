import random

brands_of_car = {
    "BMW" : {"fuel":100, "strength":100, "consumption":6},
    "Volvo" : {"fuel":75, "strength":60, "consumption":8},
    "ЗАЗ" : {"fuel":45, "strength":30, "consumption":15},
    "Ford" : {"fuel":80, "strength":130, "consumption":4}
}

job_list = {
    "Java dev" : {"salary":50, "gladness_less":10},
    "Python dev" : {"salary":40, "gladness_less":3},
    "Assembler dev" : {"salary":1000, "gladness_less":25},
    "Swift dev" : {"salary":44, "gladness_less":2}

}

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)


    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive:
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

    def shopping(self, manage):
        if self.car.drive:
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.car.fuel += 50
            self.money -= 50
        elif manage == "food":
            print("I bought foods")
            self.money -= 30
            self.home.food += 30
        elif manage == "delicacies":
            print("I bought delicacies")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def day_index(self, day):
        print(f"Today the {day} of {self.name}")
        print(f"money = {self.money} $\tsatiety = {self.satiety}\tgladness = {self.gladness}")
        print("-"* 35)
        print(f"food in home = {self.home.food}\tmess in home = {self.home.mess}")
        print("-" * 35)
        print(f"Fuel - {self.car.fuel}\tStrength = {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead..")
            return  False
        if self.money < -500:
            print("Bankrot")
            return  False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("set home")
            self.get_home()
        if self.car is None:
            print("set car")
            self.get_car()
        if self.job is None:
            self.get_job()
            print(f"I got job {self.job.job} with salary {self.job.salary}")
        self.day_index(100)
        #Доробіть  симуліцію життя персонажа в цьому методі напишіть код нижче


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brands_of_car[self.brand]["fuel"]
        self.strength = brands_of_car[self.brand]["strength"]
        self.consumption = brands_of_car[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cant move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


nick = Human(name="Nick")

for  day in range(1, 8):
    if nick.live(day) == False:
        break