import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/suppliers/12/products")
        self._response = requests.get(get_path)
        self._expected_response = [
            {
                "ProductID": 77,
                "ProductName": "Original Frankfurter grüne Soße",
                "Category": {"CategoryID": 2, "CategoryName": "Condiments"},
                "Discontinued": 0,
            },
            {
                "ProductID": 75,
                "ProductName": "Rhönbräu Klosterbier",
                "Category": {"CategoryID": 1, "CategoryName": "Beverages"},
                "Discontinued": 0,
            },
            {
                "ProductID": 64,
                "ProductName": "Wimmers gute Semmelknödel",
                "Category": {"CategoryID": 5, "CategoryName": "Grains/Cereals"},
                "Discontinued": 0,
            },
            {
                "ProductID": 29,
                "ProductName": "Thüringer Rostbratwurst",
                "Category": {"CategoryID": 6, "CategoryName": "Meat/Poultry"},
                "Discontinued": 1,
            },
            {
                "ProductID": 28,
                "ProductName": "Rössle Sauerkraut",
                "Category": {"CategoryID": 7, "CategoryName": "Produce"},
                "Discontinued": 1,
            },
        ]

    def test_status_code(self):
        self.assertEqual(self._response.status_code, 200)

    def test_response(self):
        self.assertEqual(
            self._response.json(),
            self._expected_response,
        )


if __name__ == "__main__":
    unittest.main()
