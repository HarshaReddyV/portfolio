list =[]
while True:
    try:
        name = input('Name:')
        list.append(name)
    except EOFError:

        n = len(list)
        if n == 1:
             print('Adieu, adieu, to',list[0])
             exit()

        if n==2:
            print(f'Adieu, adieu, to {list[0]} and {list[1]}')
            exit()

        print('Adieu, adieu, to ',end='')
        p =0
        for i in range(n-1):
            print(f'{list[p]}, ',end ='')
            p = p +1

        print('and',list[n-1])
        exit()