#  Створити додаток "Домовий менеджмент". Основне завдання проєкту — надати користувачеві можливість зберігати
#  інформацію про мешканців будинку.

# Інтерфейс додатка має надавати такі можливості:
# Додавання мешканців будинку.
# Видалення мешканців будинку.
# Додавання квартир (обов'язкова наявність можливості додавати інформацію про поверх).
# Видалення квартир.
# Закріплення мешканців за квартирою.
# Відкріплення мешканців від квартири.
# Збереження інформації у файл.
# Завантаження інформації з файлу.
# Створення звітів за такими параметрами:
# Відображення повного списку мешканців;
# Відображення повного списку квартир;
# Відображення інформації про конкретну квартиру;
# Відображення інформації про квартири на конкретному поверсі;
# Відображення інформації про квартири одного типу (наприклад, відобразити всі однокімнатні квартири).
# Правильне використання патернів проєктування, принципів SOLID, механізмів тестування під час реалізації завдання
# дасть змогу отримати вищу оцінку.

class Person:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.surname}, Phone: {self.phone}"

class Apartment:
    def __init__(self, number, floor, type):
        self.number = number
        self.floor = floor
        self.type = type
        self.residents = []


class DataService:
    pass

class ReportService:
   pass


def main():
    data_service = DataService()
    report_service = ReportService()
    apartments = data_service.load_data()