import random
while True:
    try:
        n =int(input('Level:'))
        if n>0:
            break
    except:
        pass


p = random.randint(1,n)

while True:
    try:
        x = int(input('Guess:'))
        if x >p:
            print('Too Large!')
        elif x<p:
            print('Too small!')
        elif x == p:
            print('Just Right!')
            exit()
    except ValueError:
        continue