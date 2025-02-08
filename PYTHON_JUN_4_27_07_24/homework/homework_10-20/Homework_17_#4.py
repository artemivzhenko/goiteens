import datetime

def is_leap_year(year):
    """
    Перевіряє, чи є рік високосним.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_between_dates(date1, date2):
    """
    Обчислює кількість днів між двома датами.
    """
    d1 = datetime.strptime(date1, "%d-%m-%Y")
    d2 = datetime.strptime(date2, "%d-%m-%Y")
    delta = d2 - d1
    return abs(delta.days)

def format_date(date):
    """
    Форматує дату у вигляді "DD-MM-YYYY".
    """
    d = datetime.strptime(date, "%Y-%m-%d")
    return d.strftime("%d-%m-%Y")
