image = ('gif','jpg','jpeg','png')
app = ('pdf','zip','txt')

x = input('File name:')
x = x.lower()
x = x.strip()
for l in image:
    if l in x:
        if l == 'jpg' or l == 'jpeg':
            print('image/jpeg')
            exit()
        print(f'image/{l}')
        exit()

for m in app:
    if m in x:
        if m == 'txt':
            print('text/plain')
            exit()
        print(f'application/{m}')
        exit()

print('application/octet-stream')
