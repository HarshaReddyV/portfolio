lists={}
while True:
    try:
        item = input()
        item = item.upper()
        if item in lists.keys():
            lists[item] += 1
        else:
            lists[item] = 1
    except EOFError:
       new = list(lists.keys())
       new.sort()
       final ={}
       for i in new:
           final[i] = lists[i]
       for key,values in final.items():
            print(values,key)
       exit()
