import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        self.input_data = {
            "CompanyName": "Test Company Name",
        }
        self.update_data = {"ContactName": "Test Contact", "ContactTitle": "Test Title"}

    def test_update(self):
        post_path = urllib.parse.urljoin(AppClass.APP_URL, "/suppliers")
        post_response = requests.post(post_path, json=self.input_data)
        post_response_json = post_response.json()
        record_id = post_response_json.get("SupplierID")
        self.assertIsInstance(record_id, int)

        put_path = urllib.parse.urljoin(AppClass.APP_URL, f"/suppliers/{record_id}")
        put_response = requests.put(put_path, json=self.update_data)
        put_response_json = put_response.json()
        self.assertEqual(
            put_response_json.get("CompanyName"), self.input_data["CompanyName"]
        )
        self.assertEqual(
            put_response_json.get("ContactName"), self.update_data["ContactName"]
        )
        self.assertEqual(
            put_response_json.get("ContactTitle"), self.update_data["ContactTitle"]
        )

        get_path = urllib.parse.urljoin(AppClass.APP_URL, f"/suppliers/{record_id}")
        get_response = requests.get(get_path)
        get_response_json = get_response.json()
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(
            get_response_json.get("CompanyName"), self.input_data["CompanyName"]
        )
        self.assertEqual(
            get_response_json.get("ContactName"), self.update_data["ContactName"]
        )
        self.assertEqual(
            get_response_json.get("ContactTitle"), self.update_data["ContactTitle"]
        )

    def test_create(self):
        put_path = urllib.parse.urljoin(AppClass.APP_URL, "/suppliers/999")
        put_response = requests.put(put_path, json={"CompanyName": "Test Company Name"})
        self.assertEqual(put_response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
