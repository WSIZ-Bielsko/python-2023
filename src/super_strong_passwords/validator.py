def check_password_validity(password: str, username: str = '##################') -> bool:
    # Check length
    if len(password) < 12:
        return False

    # Check for at least one number
    if not any(char.isdigit() for char in password):
        return False

    # Check for at least one symbol
    if not any(char in "!#$%&*+-=?@^_|~" for char in password):
        return False

    # Check first character is not a symbol
    if password[0] in "!#$%&*+-=?@^_|~":
        return False

    # Check no character repeats more than twice in sequence
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return False

    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check for forbidden values
    forbidden_values = ["`", "@", "css", "ä", "Ä", "test", "§", "script", "°",
                        "password", "´", "ö", "Ö", "xss", "html", "Ü", "ü", "<", "^", ">", "ß"]
    if any(value in password for value in forbidden_values):
        return False

    # exclude parts of username of len >= 3
    excluded_parts = []
    for ln in range(3, len(username)):
        for st in range(0, len(username) - ln + 1):
            excluded_parts.append(username[st:st + ln])
    if any(value in password for value in excluded_parts):
        return False

    # Check if password has been used previously (this would require a history check)
    # For demonstration, assume no history is available

    return True


