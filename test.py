import unittest
from unittest.mock import patch
from src.rdapi import RD  # Import your RD class from your script
import dotenv


class TestRDMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rd = RD()

    def test_check_token_valid(self):
        self.assertIsNone(self.rd.check_token())

    def test_check_token_invalid(self):
        with self.assertLogs(level='WARNING') as cm:
            self.rd.check_token()
        self.assertIn("WARNING:root:Add token to .env", cm.output)

    @patch('requests.get')
    def test_get_system_time(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"time": "2023-09-27T12:00:00Z"}

        response = self.rd.system.time()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["time"], "2023-09-27T12:00:00Z")

    @patch('requests.get')
    def test_get_system_time_error(self, mock_get):
        mock_get.return_value.status_code = 500

        response = self.rd.system.time()
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()
