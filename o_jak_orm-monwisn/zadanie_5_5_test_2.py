import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def test_delete(self):
        del_path = urllib.parse.urljoin(AppClass.APP_URL, f"/suppliers/998")
        del_response = requests.delete(del_path)
        self.assertEqual(del_response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
