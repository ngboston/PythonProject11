#  Шостий варіант
# Створити додаток "Домовий менеджмент". Основне завдання проєкту — надати користувачеві можливість зберігати інформацію про мешканців будинку.
#
# Інтерфейс додатка має надавати такі можливості:
#
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
# Правильне використання патернів проєктування, принципів SOLID, механізмів тестування під час реалізації завдання дасть змогу отримати вищу оцінку.

import json

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

    def add_resident(self, person):
        self.residents.append(person)

    def remove_resident(self, person):
        self.residents.remove(person)

    def __str__(self):
        return f"Apartment {self.number}, Floor: {self.floor}, Type: {self.type}, Residents: {', '.join(str(r) for r in self.residents)}"

class DataService:
    def __init__(self, filename="house_data.json"):
        self.filename = filename

    def save_data(self, apartments):
        data = []
        for apartment in apartments:
            apartment_data = {
                "number": apartment.number,
                "floor": apartment.floor,
                "type": apartment.type,
                "residents": [{"name": r.name, "surname": r.surname, "phone": r.phone} for r in apartment.residents]
            }
            data.append(apartment_data)

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return []

        apartments = []
        for apartment_data in data:
            apartment = Apartment(apartment_data["number"], apartment_data["floor"], apartment_data["type"])
            for resident_data in apartment_data["residents"]:
                person = Person(resident_data["name"], resident_data["surname"], resident_data["phone"])
                apartment.add_resident(person)
            apartments.append(apartment)

        return apartments


class ReportService:
    def generate_residents_report(self, apartments):
        residents = []
        for apartment in apartments:
            residents.extend(apartment.residents)
        return "\n".join(str(r) for r in residents)

    def generate_apartments_report(self, apartments):
        return "\n".join(str(a) for a in apartments)

    def generate_apartment_info(self, apartments, apartment_number):
        for apartment in apartments:
            if apartment.number == apartment_number:
                return str(apartment)
        return "Apartment not found"

    def generate_floor_report(self, apartments, floor_number):
        floor_apartments = [a for a in apartments if a.floor == floor_number]
        return "\n".join(str(a) for a in floor_apartments)

    def generate_type_report(self, apartments, apartment_type):
        type_apartments = [a for a in apartments if a.type == apartment_type]
        return "\n".join(str(a) for a in type_apartments)

def main():
    data_service = DataService()
    report_service = ReportService()
    apartments = data_service.load_data()

    while True:
        print("\nHouse Management App")
        print("1. Add Apartment")
        print("2. Remove Apartment")
        print("3. Add Resident to Apartment")
        print("4. Remove Resident from Apartment")
        print("5. Residents Report")
        print("6. Apartments Report")
        print("7. Apartment Info")
        print("8. Floor Report")
        print("9. Type Report")
        print("10. Save and Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            number = int(input("Enter apartment number: "))
            floor = int(input("Enter floor number: "))
            type = input("Enter apartment type: ")
            apartments.append(Apartment(number, floor, type))
        elif choice == "2":
            number = int(input("Enter apartment number to remove: "))
            apartments = [a for a in apartments if a.number != number]
        elif choice == "3":
            number = int(input("Enter apartment number: "))
            name = input("Enter resident name: ")
            surname = input("Enter resident surname: ")
            phone = input("Enter resident phone: ")
            person = Person(name, surname, phone)
            for apartment in apartments:
                if apartment.number == number:
                    apartment.add_resident(person)
        elif choice == "4":
            number = int(input("Enter apartment number: "))
            name = input("Enter resident name to remove: ")
            for apartment in apartments:
                if apartment.number == number:
                    apartment.remove_resident(name)
        elif choice == "5":
            print(report_service.generate_residents_report(apartments))
        elif choice == "6":
            print(report_service.generate_apartments_report(apartments))
        elif choice == "7":
            number = int(input("Enter apartment number: "))
            print(report_service.generate_apartment_info(apartments, number))
        elif choice == "8":
            floor = int(input("Enter floor number: "))
            print(report_service.generate_floor_report(apartments, floor))
        elif choice == "9":
            type = input("Enter apartment type: ")
            print(report_service.generate_type_report(apartments, type))
        elif choice == "10":
            data_service.save_data(apartments)
            break

if __name__ == "__main__":
    main()