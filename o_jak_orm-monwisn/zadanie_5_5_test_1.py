import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        self.input_data = {
            "CompanyName": "Test Company Name",
        }

    def test_delete(self):
        post_path = urllib.parse.urljoin(AppClass.APP_URL, "/suppliers")
        post_response = requests.post(post_path, json=self.input_data)
        post_response_json = post_response.json()
        record_id = post_response_json.get("SupplierID")

        del_path = urllib.parse.urljoin(AppClass.APP_URL, f"/suppliers/{record_id}")
        del_response = requests.delete(del_path)
        self.assertEqual(del_response.status_code, 204)

        get_path = urllib.parse.urljoin(AppClass.APP_URL, f"/suppliers/{record_id}")
        get_response = requests.get(get_path)
        self.assertEqual(get_response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
