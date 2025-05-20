import unittest
from datetime import datetime, timedelta
from main.py import validate_user_data 

class TestUserValidation(unittest.TestCase):

    def test_valid_user(self):
        user = {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com",
            "created_at": datetime.now().isoformat()
        }
        self.assertTrue(validate_user_data(user))

    def test_missing_email(self):
        user = {
            "id": 1,
            "name": "Bob",
            "created_at": datetime.now().isoformat()
        }
        self.assertFalse(validate_user_data(user))

    def test_old_timestamp(self):
        user = {
            "id": 2,
            "name": "Old User",
            "email": "old@example.com",
            "created_at": (datetime.now() - timedelta(days=10)).isoformat()
        }
        self.assertFalse(validate_user_data(user))

    def test_invalid_email(self):