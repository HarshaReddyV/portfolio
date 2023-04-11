month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
months ={}
p =1
for i in month:
    i.lower()
    months[i] = p
    p = p+1

while True:
    date = input('Enter Date:')
    date.lower()
    try:
        if '/' in date:
            m,d,y = date.split('/')
            m = int(m)
            d = int(d)
            y = int(y)
            if m>12 or d>31:
                pass
            else:
                print(f'{y}-{m:02}-{d:02}')
                exit()
        elif ' ' in date:
            if ',' in date:
                date = date.replace(',','')
            else:
                continue
            m,d,y = date.split(' ')
            d = int(d)
            y = int(y)

            if m in month:
                m = months[m]
                if m>12 or d>31:
                    pass
                else:
                    print(f'{y}-{m:02}-{d:02}')
                    exit()

            else:
                pass
    except ValueError:
         pass




