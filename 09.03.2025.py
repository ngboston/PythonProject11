#Завдання 1
#Реалізуйте патерн Builder. Протестуйте роботу створеного класу.

print("\nTask 1")

class Computer:
    def __init__(self, cpu, ram, storage, gpu=None):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, GPU: {self.gpu}"


class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def set_gpu(self, gpu):
        self.gpu = gpu
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.storage, self.gpu)


builder = ComputerBuilder()
computer = builder.set_cpu("Intel i7").set_ram("16GB").set_storage("512GB SSD").set_gpu("NVIDIA RTX 3080").build()

print(computer)

builder = ComputerBuilder()
basic_computer = builder.set_cpu("Intel i3").set_ram("8GB").set_storage("256GB HDD").build()

print(basic_computer)

# Завдання 2
# Створіть додаток для приготування пасти. Додаток має вміти створювати щонайменше три види пасти.  Класи різної пасти мають містити такі методи:

# Тип пасти;
# Соус;
# Начинка;
# Добавки.
# Для реалізації використовуйте твірні патерни.

print("\nTask 2")

from abc import ABC, abstractmethod

class Pasta(ABC):
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sauce(self):
        pass

    @abstractmethod
    def get_filling(self):
        pass

    @abstractmethod
    def get_toppings(self):
        pass


class Spaghetti(Pasta):
    def __init__(self):
        self._type = "Спагеті"
        self._sauce = None
        self._filling = None
        self._toppings = []

    def get_type(self):
        return self._type

    def get_sauce(self):
        return self._sauce

    def get_filling(self):
        return self._filling

    def get_toppings(self):
        return self._toppings

class Ravioli(Pasta):
    def __init__(self):
        self._type = "Равіолі"
        self._sauce = None
        self._filling = None
        self._toppings = []

    def get_type(self):
        return self._type

    def get_sauce(self):
        return self._sauce

    def get_filling(self):
        return self._filling

    def get_toppings(self):
        return self._toppings

class Lasagna(Pasta):
    def __init__(self):
        self._type = "Лазанья"
        self._sauce = None
        self._filling = None
        self._toppings = []

    def get_type(self):
        return self._type

    def get_sauce(self):
        return self._sauce

    def get_filling(self):
        return self._filling

    def get_toppings(self):
        return self._toppings


class PastaBuilder(ABC):
    @abstractmethod
    def set_sauce(self, sauce):
        pass

    @abstractmethod
    def set_filling(self, filling):
        pass

    @abstractmethod
    def add_topping(self, topping):
        pass

    @abstractmethod
    def get_result(self):
        pass

class SpaghettiBuilder(PastaBuilder):
    def __init__(self):
        self._pasta = Spaghetti()

    def set_sauce(self, sauce):
        self._pasta._sauce = sauce
        return self

    def set_filling(self, filling):
        self._pasta._filling = filling
        return self

    def add_topping(self, topping):
        self._pasta._toppings.append(topping)
        return self

    def get_result(self):
        return self._pasta

class RavioliBuilder(PastaBuilder):
    def __init__(self):
        self._pasta = Ravioli()

    def set_sauce(self, sauce):
        self._pasta._sauce = sauce
        return self

    def set_filling(self, filling):
        self._pasta._filling = filling
        return self

    def add_topping(self, topping):
        self._pasta._toppings.append(topping)
        return self

    def get_result(self):
        return self._pasta

class LasagnaBuilder(PastaBuilder):
    def __init__(self):
        self._pasta = Lasagna()

    def set_sauce(self, sauce):
        self._pasta._sauce = sauce
        return self

    def set_filling(self, filling):
        self._pasta._filling = filling
        return self

    def add_topping(self, topping):
        self._pasta._toppings.append(topping)
        return self

    def get_result(self):
        return self._pasta

class Director:
    def __init__(self, builder):
        self._builder = builder

    def set_builder(self, builder):
        self._builder = builder

    def make_pasta(self, sauce, filling, toppings):
        self._builder.set_sauce(sauce)
        self._builder.set_filling(filling)
        for topping in toppings:
            self._builder.add_topping(topping)
        return self._builder.get_result()

spaghetti_builder = SpaghettiBuilder()
director = Director(spaghetti_builder)
spaghetti = director.make_pasta("Томатний соус", "Фрикадельки", ["Пармезан", "Базилік"])

print(f"Тип пасти: {spaghetti.get_type()}")
print(f"Соус: {spaghetti.get_sauce()}")
print(f"Начинка: {spaghetti.get_filling()}")
print(f"Добавки: {', '.join(spaghetti.get_toppings())}")

ravioli_builder = RavioliBuilder()
director.set_builder(ravioli_builder)
ravioli = director.make_pasta("Вершковий соус", "Сир рікотта", ["Шпинат"])

print(f"Тип пасти: {ravioli.get_type()}")
print(f"Соус: {ravioli.get_sauce()}")
print(f"Начинка: {ravioli.get_filling()}")
print(f"Добавки: {', '.join(ravioli.get_toppings())}")

lasagna_builder = LasagnaBuilder()
director.set_builder(lasagna_builder)
lasagna = director.make_pasta("Бешамель", "М'ясний фарш", ["Моцарела"])

print(f"Тип пасти: {lasagna.get_type()}")
print(f"Соус: {lasagna.get_sauce()}")
print(f"Начинка: {lasagna.get_filling()}")
print(f"Добавки: {', '.join(lasagna.get_toppings())}")


# Завдання 3
# Реалізуйте патерн Prototype. Протестуйте роботу створеного класу.

print("\nTask 3")

import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Реєструє об'єкт у прототипі."""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Видаляє об'єкт з прототипу."""
        del self._objects[name]

    def clone(self, name, **attr):
        """Клонує об'єкт з прототипу та змінює його атрибути."""
        obj = copy.deepcopy(self._objects.get(name))
        if obj:
            obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.color} {self.make} {self.model}"

prototype = Prototype()
prototype.register_object("bmw", Car("BMW", "X5", "Blue"))
prototype.register_object("toyota", Car("Toyota", "Camry", "Silver"))

car1 = prototype.clone("bmw", color="Red")
car2 = prototype.clone("toyota", model="Corolla")

print(car1)
print(car2)

