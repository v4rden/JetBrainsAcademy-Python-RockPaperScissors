user_input = input()
number = 0
cafe = ""

while user_input != "MEOW":
    info = user_input.split()
    if number < int(info[1]):
        cafe = info[0]
        number = int(info[1])
    user_input = input()

print(cafe)
