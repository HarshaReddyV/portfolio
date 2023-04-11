def main():
    x = input('Greeting:')
    result = value(x)
    print(f'${result}')


def value(x):
    x = x.strip()
    x = x.lower()
    if 'hello' in x:
        return 0
    elif x[0] == 'h':
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()







