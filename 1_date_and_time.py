#!env/bin/python3

from datetime import datetime, timedelta
from tzlocal import get_localzone

"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    local_tz = get_localzone()
    dt_now = datetime.now(local_tz).strftime('%d.%m.%Y')
    dt_yd = (datetime.now(local_tz) - timedelta(days = 1)).strftime('%d.%m.%Y')
    dt_30d_ago = (datetime.now(local_tz) - timedelta(days = 30)).strftime('%d.%m.%Y')

    print(f'Yesterday was {dt_yd}')
    print(f'Today is {dt_now}')
    print(f'30 days ago was {dt_30d_ago}')




def str_2_datetime(date_string):
    date_dstr = datetime.strptime(date_string, '%y/%m/%d %H:%M:%S.%f')
    return f'Date from string is {date_dstr}'

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
