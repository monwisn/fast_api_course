import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/suppliers/5")
        self._response = requests.get(get_path)
        self._expected_response = {
            "SupplierID": 5,
            "CompanyName": "Cooperativa de Quesos 'Las Cabras'",
            "ContactName": "Antonio del Valle Saavedra",
            "ContactTitle": "Export Administrator",
            "Address": "Calle del Rosal 4",
            "City": "Oviedo",
            "Region": "Asturias",
            "PostalCode": "33007",
            "Country": "Spain",
            "Phone": "(98) 598 76 54",
            "Fax": None,
            "HomePage": None,
        }

    def test_status_code(self):
        self.assertEqual(self._response.status_code, 200)

    def test_response(self):
        self.assertEqual(
            self._response.json(),
            self._expected_response,
        )

    def test_not_exists(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/suppliers/31")
        response = requests.get(get_path)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
