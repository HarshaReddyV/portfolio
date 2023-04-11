m = input('Expression:')
x,y,z = m.split(' ')

g = x + y + z
g = eval(g)
print("%.1f" % g)


