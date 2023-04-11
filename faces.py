import emoji

def main():
    voice = input("Type the emoticon....")
    convert(voice)


def convert(voice):
    voice = voice.replace(':)','\U0001f642')
    voice = voice.replace(':(','\U0001f641')
    print(voice)


main()