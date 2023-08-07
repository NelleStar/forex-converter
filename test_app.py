import unittest
from app import app

class TestConvertRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_convert_valid_input(self):
        response = self.app.post('/', data={
            'base_currency': 'USD',
            'target_currency': 'EUR',
            'amount': '100',
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Converted Amount:', response.data)

    def test_convert_invalid_input(self):
        response = self.app.post('/', data={
            'base_currency': 'XYZ',  # Invalid currency code
            'target_currency': 'EUR',
            'amount': '100',
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Not a valid code:', response.data)

if __name__ == '__main__':
    unittest.main()
