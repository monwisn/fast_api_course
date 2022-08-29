import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/suppliers")
        self._response = requests.get(get_path)
        self._expected_response = [
            {"SupplierID": 1, "CompanyName": "Exotic Liquids"},
            {"SupplierID": 2, "CompanyName": "New Orleans Cajun Delights"},
            {"SupplierID": 3, "CompanyName": "Grandma Kelly's Homestead"},
            {"SupplierID": 4, "CompanyName": "Tokyo Traders"},
            {"SupplierID": 5, "CompanyName": "Cooperativa de Quesos 'Las Cabras'"},
            {"SupplierID": 6, "CompanyName": "Mayumi's"},
            {"SupplierID": 7, "CompanyName": "Pavlova, Ltd."},
            {"SupplierID": 8, "CompanyName": "Specialty Biscuits, Ltd."},
            {"SupplierID": 9, "CompanyName": "PB Knäckebröd AB"},
            {"SupplierID": 10, "CompanyName": "Refrescos Americanas LTDA"},
            {"SupplierID": 11, "CompanyName": "Heli Süßwaren GmbH & Co. KG"},
            {"SupplierID": 12, "CompanyName": "Plutzer Lebensmittelgroßmärkte AG"},
            {
                "SupplierID": 13,
                "CompanyName": "Nord-Ost-Fisch Handelsgesellschaft mbH",
            },
            {"SupplierID": 14, "CompanyName": "Formaggi Fortini s.r.l."},
            {"SupplierID": 15, "CompanyName": "Norske Meierier"},
            {"SupplierID": 16, "CompanyName": "Bigfoot Breweries"},
            {"SupplierID": 17, "CompanyName": "Svensk Sjöföda AB"},
            {"SupplierID": 18, "CompanyName": "Aux joyeux ecclésiastiques"},
            {"SupplierID": 19, "CompanyName": "New England Seafood Cannery"},
            {"SupplierID": 20, "CompanyName": "Leka Trading"},
            {"SupplierID": 21, "CompanyName": "Lyngbysild"},
            {"SupplierID": 22, "CompanyName": "Zaanse Snoepfabriek"},
            {"SupplierID": 23, "CompanyName": "Karkki Oy"},
            {"SupplierID": 24, "CompanyName": "G'day, Mate"},
            {"SupplierID": 25, "CompanyName": "Ma Maison"},
            {"SupplierID": 26, "CompanyName": "Pasta Buttini s.r.l."},
            {"SupplierID": 27, "CompanyName": "Escargots Nouveaux"},
            {"SupplierID": 28, "CompanyName": "Gai pâturage"},
            {"SupplierID": 29, "CompanyName": "Forêts d'érables"},
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
