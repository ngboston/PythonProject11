import unittest
from models.apartment import Apartment
from models.person import Person
from services.report_service import ReportService

class TestReportService(unittest.TestCase):
    def setUp(self):
        self.report_service = ReportService()
        self.apartments = [
            Apartment(1, 3, "1-bedroom"),
            Apartment(2, 5, "2-bedroom")
        ]
        self.apartments[0].add_resident(Person("John", "Doe", "123-456-7890"))

    def test_generate_residents_report(self):
        report = self.report_service.generate_residents_report(self.apartments)
        self.assertIn("John Doe", report)

    def test_generate_apartments_report(self):
        report = self.report_service.generate_apartments_report(self.apartments)
        self.assertIn("Apartment 1", report)
        self.assertIn("Apartment 2", report)

    def test_generate_apartment_info(self):
        report = self.report_service.generate_apartment_info(self.apartments, 1)
        self.assertIn("Apartment 1", report)

    def test_generate_floor_report(self):
        report = self.report_service.generate_floor_report(self.apartments, 3)
        self.assertIn("Apartment 1", report)
        self.assertNotIn("Apartment 2", report)

    def test_generate_type_report(self):
        report = self.report_service.generate_type_report(self.apartments, "2-bedroom")
        self.assertIn("Apartment 2", report)
        self.assertNotIn("Apartment 1", report)

if __name__ == '__main__':
    unittest.main()