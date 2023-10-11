import calendar
import secrets


def month_total_days(month, year):
    return calendar.monthrange(year, month)[1]


def get_random_password():
    password_length = 13
    return secrets.token_urlsafe(password_length)
