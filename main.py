import re
import logging
from datetime import datetime, timedelta


logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')



def is_valid_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_recent_timestamp(timestamp):
    try:
        date = datetime.fromisoformat(timestamp)
        return datetime.now() - date <= timedelta(days=7)
    except ValueError:
        return False

def validate_user_data(data):
    try:
        
        if not isinstance(data.get('id'), int):
            logging.error("Invalid or missing 'id'")
            return False

        if not isinstance(data.get('name'), str):
            logging.error("Invalid or missing 'name'")
            return False

        if not isinstance(data.get('email'), str) or not is_valid_email(data['email']):
            logging.error("Invalid or missing 'email'")
            return False

        if not isinstance(data.get('created_at'), str) or not is_recent_timestamp(data['created_at']):
            logging.error("Invalid or old 'created_at'")
            return False

        return True

    except Exception as e:
        logging.error(f"Unexpected error during validation: {e}")
        return False


def fetch_user():
        return {
        "id": 1,
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "created_at": datetime.now().isoformat()
    }
if __name__ == "__main__":
    user_data = fetch_user()
    is_valid = validate_user_data(user_data)
    print("Is valid user?", is_valid)
