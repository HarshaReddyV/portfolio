from pyfiglet import Figlet
import sys
import random

n = len(sys.argv)
figlet = Figlet()
fonts = figlet.getFonts()

if n ==1:
    s = input('Enter Text:')
    f = random.choice(fonts)
    figlet.setFont(font=f )
    print(figlet.renderText(s))
    pass
elif n ==3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        pass
    else:
        sys.exit('Invalid Usage')


    f = sys.argv[2]
    print(f)

    if f not in fonts:
        sys.exit('Invalid Usage')
    else:
        s = input('Enter Text:')
        figlet.setFont(font = f)
        print(figlet.renderText(s))

else:
    sys.exit('Invalid Usage')





