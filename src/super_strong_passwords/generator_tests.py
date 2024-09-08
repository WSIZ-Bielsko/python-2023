import string

import pytest

from src.super_strong_passwords.generator import generate_password
from src.super_strong_passwords.validator import check_password_validity


# Test 1-5: Check length
def test_password_length():
    for _ in range(500):
        password = generate_password()
        assert len(password) >= 12


# Test 6-10: Check for at least one lowercase letter
def test_password_lowercase():
    for _ in range(500):
        password = generate_password()
        assert any(c.islower() for c in password)


# Test 11-15: Check for at least one uppercase letter
def test_password_uppercase():
    for _ in range(500):
        password = generate_password()
        assert any(c.isupper() for c in password)


# Test 16-20: Check for at least one digit
def test_password_digit():
    for _ in range(500):
        password = generate_password()
        assert any(c.isdigit() for c in password)


# Test 21-25: Check for at least one symbol
def test_password_symbol():
    symbols = '!#$%&*+-./:;=?@[]^_`{|}~'
    for _ in range(500):
        password = generate_password()
        assert any(c in symbols for c in password)


# Test 26: First character is not a symbol
def test_password_first_character():
    for _ in range(500):
        password = generate_password()
        assert password[0] in (string.ascii_letters + string.digits)


# Test 27: No character repeats more than twice
def test_password_no_repeating_characters():
    for _ in range(500):
        password = generate_password()
        assert not any(password[i] == password[i + 1] == password[i + 2] for i in range(len(password) - 2))


# Test 28: Does not include invalid values
def test_password_no_invalid_values():
    invalid_values = ["`", "@", "css", "ä", "Ä", "test", "§", "script", "°",
                      "password", "´", "ö", "Ö", "xss", "html", "Ü", "ü", "<", "^", ">", "ß"]
    for _ in range(500):
        password = generate_password()
        assert not any(value in password for value in invalid_values)


# Test 29: Validate generated password
def test_generated_password_is_valid():
    for _ in range(500):
        password = generate_password()
        assert check_password_validity(password)


# Test 30: Check password uniqueness (example test)
def test_password_uniqueness():
    passwords = set()
    for _ in range(500):
        password = generate_password()
        assert password not in passwords
        passwords.add(password)
