import json
import os

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

        try:
            with open(self.filename, "w") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def load_data(self):
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data from file: {e}")
            return []

        apartments = []
        for apartment_data in data:
            apartment = Apartment(apartment_data["number"], apartment_data["floor"], apartment_data["type"])
            for resident_data in apartment_data["residents"]:
                person = Person(resident_data["name"], resident_data["surname"], resident_data["phone"])
                apartment.add_resident(person)
            apartments.append(apartment)

        return apartments