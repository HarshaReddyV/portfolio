import sys
import os.path


if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) == 1:
    sys.exit('Too few command-line arguments')
elif '.py' not in sys.argv[1]:
    sys.exit('Not a Python file')
elif os.path.isfile(sys.argv[1]) == False:
    sys.exit(f'Could not read {sys.argv[1]}')

file = sys.argv[1]

code=[]
try:
    with open(file, 'r') as File:
        for line in File:
            if line.isspace()==True:
                continue

            line = line.lstrip()

            if line.startswith('#') or line.startswith(' #'):
                continue


            code.append(line.strip())

except(FileNotFoundError):
    sys.exit()



print(len(code))

