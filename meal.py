def main():
    x = input('Enter Time:')
    x = convert(x)
    if x>=7 and x<=8:
        print('breakfast time')
    elif x>=12 and x<=13:
        print('lunch time')
    elif x>=18 and x<=19:
        print('dinner time')

def convert(time):

    hours,min = time.split(":")
    hours = int(hours)
    min = int(min)
    min = min/60
    x = hours + min
    return x

if __name__ == "__main__":
    main()