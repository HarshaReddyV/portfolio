import re
from tabulate import tabulate
from datetime import date
import sys
import random

days_month = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}



def main():
    day = get_Date(input('Enter Date DD-MM-YYYY:').strip())

    print(tabulate([[day, get_Time(), get_service()]], headers=['Booking Date','Appointment Time','Service'], tablefmt="double_grid"))


def get_Date(d):
    try:
        r = re.fullmatch(r"^([0-3][0-9])-([0-1][0-9])-([0-9][0-9][0-9][0-9])$",d)
        day = int(r.group(1))
        month = int(r.group(2))
        year = int(r.group(3))

        if month == 2 and year%4 == 0:
            if day>29:
                print('Invalid Day in Feb')
                exit()
        elif day > days_month[month]:
            print('Invalid Day in Month')
            exit()

        booking_day = date(year,month,day)
        today = date.today()

        t = booking_day - today
        if t.days < 1:
            print('Day has to be in future')
            exit()
        else:
            return booking_day

    except:
        sys.exit('Invalid Date format')


def get_Time():
    times = ['9:00','9:30','10:00','10:30','12:00','13:00','16:00']
    t = random.choice(times)
    return t


def get_service():
    event = ['Hair cut','Shave','Trim', 'Massage','Wax','Pedicure','Manicure','Cut and Colouring','Aroma-Therapy']
    s = random.choice(event)
    return s


if __name__ == "__main__":
    main()