#!/usr/bin/env python

from datetime import date, datetime, timedelta
from typing import Tuple
from calendar import Calendar


class CheckingsException(Exception):
    pass

class InvalidCheckingsNumber(CheckingsException):
    pass

class InvalidCheckingsOrder(CheckingsException):
    pass


def simple_code_generator(code_lenght:int) -> int:
    from random import randint

    low_range = 10**(code_lenght-1)
    high_range = (10**code_lenght)-1
    return randint(low_range, high_range)

def qrcode_generator(code:int):
    import qrcode

    qr = qrcode.QRCode(version=1, box_size=25, border=1)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode.png')
#qrcode_generator(simple_code_generator(5))

def work_time_calculator(checkings:list)-> Tuple[int, int]:
    time_worked = timedelta()

    for i in range(0, len(checkings), 2):
        check_in = checkings[i].datetime
        check_out = checkings[i+1].datetime
        time_worked += check_out - check_in        

    # hours, minutes = time_worked.seconds // 3600, round(time_worked.seconds % 3600 / 60.0)
    return time_worked

def check_checkings(checkings:list) -> None:
    if len(checkings) % 2 != 0:
        raise InvalidCheckingsNumber()

    for (index, checking) in enumerate(checkings):
        if checking.check % 2 != index % 2:
            raise InvalidCheckingsOrder()
        if index > 0 and checkings[index - 1].datetime > checkings[index].datetime:
            raise InvalidCheckingsOrder()

# a = datetime.now(days = -2)

# a = datetime(year = 2021, month=10, day = 17, hour = 8, minute = 0)
# b = datetime(year = 2021, month=10, day = 17, hour = 12, minute = 0)
# c = datetime(year = 2021, month=10, day = 17, hour = 14, minute = 0)
# d = datetime(year = 2021, month=10, day = 17, hour = 18, minute = 0, second = 59)

horaires = [Calendar(id=i, user=0, datetime=(datetime(year = 2021, month=10, day = 17, hour = 8, minute = 0) + timedelta(minutes=i)), month=10, year=2021, check=i % 2) for i in range(7_200_000)]
print(len(horaires))

# horaires = [
#     Calendar(id = 0, user = 0, datetime=a, month = 10, year = 2021, check = 0),
#     Calendar(id = 1, user = 0, datetime=b, month = 10, year = 2021, check = 1),
#     Calendar(id = 2, user = 0, datetime=c, month = 10, year = 2021, check = 0),
#     Calendar(id = 3, user = 0, datetime=d, month = 10, year = 2021, check = 1),
#     ]

import time
start_time = time.time()
check_checkings(horaires)
print(f"Took: {time.time() - start_time}")
print(work_time_calculator(horaires))