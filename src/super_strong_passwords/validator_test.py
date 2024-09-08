from src.super_strong_passwords.validator import check_password_validity


def test_simple_valid_password():
    pwd = 'aA#0123456789'
    assert check_password_validity(pwd, 'test') is True


def test_simple_valid_password_with_username():
    pwd = 'aA#0123456789test'
    assert check_password_validity(pwd, 'test') is False


def test_simple_valid_password_with_username_3chars():
    pwd = 'aA#0123456789tes'
    assert check_password_validity(pwd, 'test') is False


def test_simple_valid_password_with_username_2chars():
    pwd = 'aA#0123456789te'
    assert check_password_validity(pwd, 'test') is True


# --------- generated

# Test 1: Check minimum length
def test_password_minimum_length():
    assert not check_password_validity("Short1!")


# Test 2: Check presence of at least one number
def test_password_requires_number():
    assert not check_password_validity("Password!@#")


# Test 3: Check presence of at least one symbol
def test_password_requires_symbol():
    assert not check_password_validity("Password123")


# Test 4: Check first character is not a symbol
def test_password_first_character_not_symbol():
    assert not check_password_validity("!Password123")


# Test 5: Check no character repeats more than twice
def test_password_no_repeating_characters():
    assert not check_password_validity("Paaaassword123!")


# Test 6: Check presence of at least one lowercase letter
def test_password_requires_lowercase():
    assert not check_password_validity("PASSWORD123!")


# Test 7: Check presence of at least one uppercase letter
def test_password_requires_uppercase():
    assert not check_password_validity("password123!")


# Test 8: Check forbidden values
def test_password_no_invalid_values():
    assert not check_password_validity("Password123@")


# Test 9: Check password does not include part of the username
def test_password_no_username_part():
    username = "user"
    password = "userPassword123!"
    assert not check_password_validity(password, username)


# Test 10: Check valid password
def test_valid_password():
    assert check_password_validity("ValidPass123!")
