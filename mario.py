from cs50 import get_int

while True:
    p = get_int("size of pyramid: ")
    if p >= 1 and p<=8:
      break

y = 1
for i in range(p):
    x= p-1
    print(" "*x,"#"*y, end="\n")
    y = y+1
    p = p-1
