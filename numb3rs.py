import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        l = ip.split('.')
        if len(l) != 4:
            return False

        for i in l:
            i = int(i)
            if i <0 or i>255:
                return False
            else:
                continue
        return True
    except ValueError:
        return False



if __name__ == "__main__":
    main()