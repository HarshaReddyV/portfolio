from random import randint


def main():
    l = get_level()

    score = 0
    fail =0
    for x in range(10):
        n = generate_integer(l)
        m = generate_integer(l)
        i = n + m
        a= int(input(f'{n} + {m} = '))
        if a == i:
            score +=1
            continue
        else:
            print('EEE')
            for y in range(2):
                a= int(input(f'{n} + {m} = '))
                if a == i:
                    score+=1
                    break
                else:
                    fail+=1
                    if fail ==2:
                        print(f'{n} + {m} = {i}')
                        fail = 0
                        break
                    continue

    print('Score:',score)


def get_level():
     while True:
        try:
            l = int(input('Level:'))
            if l>0 and l<=3:
                return l
            else:
                continue
        except ValueError:
            pass


def generate_integer(n):
    if n ==1:
        return randint(0,9)
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



if __name__ == "__main__":
    main()