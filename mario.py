from cs50 import get_int

while True:
    p = get_int("size of pyramid: ")
    if p >= 1 and p <= 8:
        break

y = 1
for i in range(p):
    x = p - y
    print(" "*x, end="")

    print("#"*y, end="")

    print("  ", end="")

    print("#"*y, end="\n")

    y = y + 1