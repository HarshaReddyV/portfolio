from datetime import date
import re
import sys
import inflect


def main():

    that_day = input('Enter Date as YYYY-MM-DD:').strip()

    print(sort(that_day))



def sort(that_day):
    try:
        if r := re.fullmatch(r"^([0-9][0-9][0-9][0-9])-([0-9][0-9])-([0-9][0-9])$", that_day):
            year = int(r.group(1))
            month = int(r.group(2))
            day = int(r.group(3))

            if month>12 or day>31:
                sys.exit()

            if month==2 and day>29:
                sys.exit()
        else:
            sys.exit()
    except:
        sys.exit()

    this_day = date.today()
    that_day = date(year,month,day)

    total = this_day - that_day
    total = (total.days)*24*60
    p = inflect.engine()
    final = p.number_to_words(total, andword="")
    return (final+' minutes').capitalize()








if __name__ == "__main__":
    main()