import calendar


def month_total_days(month, year):
    return calendar.monthrange(year, month)[1]
