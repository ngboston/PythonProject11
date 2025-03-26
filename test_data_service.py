import unittest
import os
from models.apartment import Apartment
from models.person import Person
from services.data_service import DataService

class TestDataService(unittest.TestCase):
    def setUp(self):
        self.data_service = DataService("test_data.json")
        self.apartments = [
            Apartment(1, 3, "1-bedroom"),
            Apartment(2, 5, "2-bedroom")
        ]
        self.apartments[0].add_resident(Person("John", "Doe", "123-456-7890"))

    def tearDown(self):
        if os.path.exists("test_data.json"):
            os.remove("test_data.json")

    def test_save_and_load_data(self):
        self.data_service.save_data(self.apartments)
        loaded_apartments = self.data_service.load_data()
        self.assertEqual(len(loaded_apartments), 2)
        self.assertEqual(loaded_apartments[0].number, 1)
        self.assertEqual(len(loaded_apartments[0].residents), 1)

if __name__ == '__main__':
    unittest.main()