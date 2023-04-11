import re
import sys


def main():
    print(parse(input("HTML: ")))

#<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
#http://youtube.com/embed/xvFZjo5PgG0
#https://youtube.com/embed/xvFZjo5PgG0
#https://www.youtube.com/embed/xvFZjo5PgG0

def parse(s):
     s = s.strip()
     if r := re.search("<iframe src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s):
         return (f'https://youtu.be/{r.group(1)}')





if __name__ == "__main__":
    main()