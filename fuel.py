def main():
   while True:
      try:
         level = input('Level:')
         l = convert(level)
         if l == ValueError or l == ZeroDivisionError or l == None:
            continue
         l = gauge(l)
         print(l)
         exit()
      except ValueError:
         pass


def convert(level):
    try:
       x,y = level.split('/')
       x =int(x)
       y=int(y)
       if x > y :
          if y ==0:
            return None
          return None
       else:
         try:
            l = round((x/y)*100)
         except ZeroDivisionError:
            raise ZeroDivisionError
       return l
    except ValueError:
       raise ValueError

def gauge(l):
    l = int(l)
    if l <= 1:
      return'E'
    elif l >=99:
      return'F'
    else:
      return f'{l}%'


if __name__ == "__main__":
    main()







