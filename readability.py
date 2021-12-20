from cs50 import get_string

p = get_string("Enter the words here: ")

words = 0
letters = 0
sent = 0

for i in range(len(p)):
    if p[i].isalpha() == True:
        letters += 1
    if i==0 or p[i] == " " and p[i+1] != " ":
        words += 1
    if p[i] == "." or p[i] == "." or p[i] =="?" or p[i] =="!":
        sent += 1

l = (letters/words) * 100
s = (sent/words) * 100
score = round(0.0588 * l - 0.296 * s - 15.8)

if score < 1:
    print("Before grade 1")
if score > 16:
    print("Grade 16+")
else:
    print(f"Grade{score}")
