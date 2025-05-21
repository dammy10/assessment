import unittest
from datetime import datetime, timedelta
from main.py import validate_user_data 

class TestUserValidation(unittest.TestCase):

    def test_valid_user(self):
        user = {
            "id": 1,
            "name": "Dave",
            "email": "dave.ade@example.com",
            "created_at": datetime.now().isoformat()
        }
        self.assertTrue(validate_user_data(user))

    def test_missing_email(self):
        user = {
            "id": 1,
            "name": "Dave",
            "created_at": datetime.now().isoformat()
        }
        self.assertFalse(validate_user_data(user))

    def test_old_timestamp(self):
        user = {
            "id": 1,
            "name": "Dave",
            "email": "dave.ade@example.com",
            "created_at": (datetime.now() - timedelta(days=9)).isoformat()
        }
        self.assertFalse(validate_user_data(user))

    if __name__ == '__main__':
    unittest.main()
