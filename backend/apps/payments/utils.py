import secrets


def get_random_password():
    password_length = 13
    return secrets.token_urlsafe(password_length)


def get_price_in_cents(price):
    return price * 100
