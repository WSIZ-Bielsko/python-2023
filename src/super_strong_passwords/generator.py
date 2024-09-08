import random
import string

from src.super_strong_passwords.validator import check_password_validity


def generate_password():
    # todo:  gpt-4o solution (does not care about special values, username etc); use your own
    while True:
        # Generate a password with the required length and character types
        password = ''.join(random.choices(
            string.ascii_letters + string.digits + "!#$%&*+-=?@^_|~", k=12))

        # Ensure it meets all criteria
        if (check_password_validity(password)):
            return password
