word = input()

result = ""

for char in word:
    if char.islower():
        result += char
    else:
        if len(result) > 0:
            result += "_"
        result += char.lower()

print(result)
