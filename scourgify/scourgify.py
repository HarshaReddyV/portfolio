import sys
import os.path
import csv


if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) == 1:
    sys.exit('Too few command-line arguments')
elif '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:
    sys.exit('Not a CSV file')
elif os.path.isfile(sys.argv[1]) == False:
    sys.exit('File does not exist')



before = sys.argv[1]
after = sys.argv[2]

data={}

try:
    with open(before, newline='') as before_file:
        reader = csv.DictReader(before_file)
        for row in reader:
            name = row['name']
            house = row['house']
            f_name,l_name = name.split(',')
            data['first'] = f_name
            data['last'] = l_name
            data['house'] = house


            with open(after, 'a', newline='') as after_file:

                writer = csv.DictWriter(after_file)
                writer.writeheader('first','last','house')
                writer.writerow({'first': f_name, 'last': l_name,'house': house})

except(FileNotFoundError):
    sys.exit()