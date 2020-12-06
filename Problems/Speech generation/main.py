phone_number = input()

for number in phone_number:
    digit = "zero"
    if number == "1":
        digit = "one"
    if number == "2":
        digit = "two"
    if number == "3":
        digit = "three"
    if number == "4":
        digit = "four"
    if number == "5":
        digit = "five"
    if number == "6":
        digit = "six"
    if number == "7":
        digit = "seven"
    if number == "8":
        digit = "eight"
    if number == "9":
        digit = "nine"

    print(digit)
