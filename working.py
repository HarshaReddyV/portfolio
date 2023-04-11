import re
import sys


def main():
    print(convert(input("Hours: ")))

#9:00 AM to 5:00 PM
#9 AM to 5 PM

# 9:00 AM/PM
# 9 AM/PM
# 09 AM/PM

def convert(s):

    s = s.strip()
    #regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    regex = "(0?[1-9]|1?[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    try:
            r = re.search(r"^" + regex + " to " +regex+ "$",s)
    except ValueError:
            raise ValueError

    try:
        s_hr = int(r.group(1))
        s_sy = r.group(3)

        if r.group(2) is None:
             s_mi = 0
        else:
             s_mi = int(r.group(2))

        e_hr = int(r.group(4))
        e_sy = r.group(6)

        if r.group(5) is None:
             e_mi = 0
        else:
             e_mi = int(r.group(5))

    except:
         raise ValueError




    if s_sy == 'AM' and s_hr == 12:
        s_hr = 0
    elif s_sy == 'PM' and s_hr == 12:
         s_hr == 12
    elif s_sy == 'PM':
         s_hr = s_hr + 12

    if e_sy == 'PM' and e_hr == 12:
        e_hr = 12
    elif e_sy == 'AM' and e_hr == 12:
         e_hr = 0
    elif e_sy == 'PM':
         e_hr = e_hr + 12


    return (f'{s_hr:02}:{s_mi:02} to {e_hr:02}:{e_mi:02}')



if __name__ == "__main__":
    main()