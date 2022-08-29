import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        self.input_data = {
            "CompanyName": "Test Company Name",
        }

    def test_create(self):
        post_path = urllib.parse.urljoin(AppClass.APP_URL, "/suppliers")
        post_response = requests.post(post_path, json=self.input_data)
        post_response_json = post_response.json()
        self.assertEqual(post_response.status_code, 201)
        self.assertIsInstance(post_response_json.get("SupplierID"), int)
        self.assertEqual(
            post_response_json.get("CompanyName"), self.input_data["CompanyName"]
        )
        self.assertEqual(post_response_json.get("ContactName"), None)
        self.assertEqual(post_response_json.get("ContactTitle"), None)
        self.assertEqual(post_response_json.get("Address"), None)
        self.assertEqual(post_response_json.get("City"), None)
        self.assertEqual(post_response_json.get("PostalCode"), None)
        self.assertEqual(post_response_json.get("Country"), None)
        self.assertEqual(post_response_json.get("Phone"), None)
        self.assertEqual(post_response_json.get("Fax"), None)
        self.assertEqual(post_response_json.get("HomePage"), None)

        get_path = urllib.parse.urljoin(
            AppClass.APP_URL, f"/suppliers/{post_response_json.get('SupplierID')}"
        )
        get_response = requests.get(get_path)
        self.assertEqual(get_response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
