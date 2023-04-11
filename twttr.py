def main():
    i = input('Enter your Tweet:')
    text = shorten(i)
    print(text)



def shorten(text):
    l =[]
    for t in text:
        if t in ('a','e','i','o','u'):
            l.append('')
        elif t in ('A','E','I','O','U'):
            l.append('')
        else:
            l.append(t)

    s = ''.join(l)
    return s


if __name__ == "__main__":
    main()