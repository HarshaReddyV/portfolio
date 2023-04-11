import os
import sys
from PIL import Image,ImageOps

l = len(sys.argv)

if l < 3:
    sys.exit('Too few command-line arguments')
elif l>3:
    sys.exit('Too many command-line arguments')


f = sys.argv[1].lower()
s = sys.argv[2].lower()

type = ['.jpg','.jpeg','.png']

first_file_type = os.path.splitext(f)
second_file_type = os.path.splitext(s)

first_file_type = first_file_type[-1]
second_file_type = second_file_type[-1]


if second_file_type not in type:
    sys.exit('Invalid Output')
elif first_file_type != second_file_type:
    sys.exit('Input and output have different extensions')
elif os.path.isfile(sys.argv[1]) == False:
    sys.exit('Input does not exist')


try:
    shirt = Image.open("shirt.png")
    model = Image.open(f)
    model = ImageOps.fit(model, shirt.size,bleed=0.0, centering=(0.5, 0.5))
    model.paste(shirt,shirt)
    model.save(s)
except(FileNotFoundError):
    pass
