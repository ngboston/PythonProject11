import unittest
from models.person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("John", "Doe", "123-456-7890")

    def test_person_creation(self):
        self.assertEqual(self.person.name, "John")
        self.assertEqual(self.person.surname, "Doe")
        self.assertEqual(self.person.phone, "123-456-7890")

    def test_person_str(self):
        expected_str = "John Doe, Phone: 123-456-7890"
        self.assertEqual(str(self.person), expected_str)

if __name__ == '__main__':
    unittest.main()