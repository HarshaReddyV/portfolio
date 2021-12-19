from cs50 import get_int

while True:
    p = 100 *  float(input("Enter the Amount-$:"))
    if p>0:
      break
coins = 0
while  p >= 25:
    p = p - 25
    coins+= 1

while p>=10:
    p = p - 10
    coins+= 1

while p>=5:
    p = p - 5
    coins+= 1
while p>=1:
    p = p - 1
    coins+= 1

print(coins)