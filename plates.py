def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Line--12 Basic Validation. Must be from 2-6 and no characters such as .,' or spaces
#Line18-20--Iterate through the length of string and find the first number and slice the string till the end using the slice method
#--- Don't forget if there are no numbers we have to make sure they are all alphabets and retun true
#Line-30-38--send this sliced string to check wether they are any alphabets present in which case that number are in between hence invalid
#--- if all the string is number we have to check wether the first number is 0 and send flase or else send true
#--- Don't worry if you didn't get it Keep Learning

def is_valid(s):
    if len(s)>6 or len(s)<2 or s[0:2].isnumeric()== True or s.isalnum() == False:
        return False
    else:
        m = ''
        for x in range(len(s)):
            if s[x].isdigit():
              if x == 1:
                  return False
              m = s[x:]
              if look(m) == True:
                  return True
              else:
                  return False
            else:
                if s.isalpha():
                    return True


def look(m):
    if m.isnumeric()== True:
        if m[0] == '0':
            return False
        else:
            return True
    else:
        return False



if __name__ == "__main__":
    main()