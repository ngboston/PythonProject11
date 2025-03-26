import unittest
from models.apartment import Apartment
from models.person import Person

class TestApartment(unittest.TestCase):
    def setUp(self):
        self.apartment = Apartment(1, 3, "1-bedroom")
        self.person1 = Person("John", "Doe", "123-456-7890")
        self.person2 = Person("Jane", "Doe", "987-654-3210")

    def test_apartment_creation(self):
        self.assertEqual(self.apartment.number, 1)
        self.assertEqual(self.apartment.floor, 3)
        self.assertEqual(self.apartment.type, "1-bedroom")
        self.assertEqual(self.apartment.residents, [])

    def test_add_resident(self):
        self.apartment.add_resident(self.person1)
        self.assertEqual(len(self.apartment.residents), 1)
        self.assertEqual(self.apartment.residents[0], self.person1)

    def test_remove_resident(self):
        self.apartment.add_resident(self.person1)
        self.apartment.add_resident(self.person2)
        self.apartment.remove_resident(self.person1)
        self.assertEqual(len(self.apartment.residents), 1)
        self.assertEqual(self.apartment.residents[0], self.person2)

    def test_apartment_str(self):
        self.apartment.add_resident(self.person1)
        expected_str = "Apartment 1, Floor: 3, Type: 1-bedroom, Residents: John Doe, Phone: 123-456-7890"
        self.assertEqual(str(self.apartment), expected_str)

if __name__ == '__main__':
    unittest.main()