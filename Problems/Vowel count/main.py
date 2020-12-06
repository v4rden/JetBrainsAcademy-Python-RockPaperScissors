string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

vowels_counter = 0

for letter in string:
    if letter in vowels:
        vowels_counter += 1

print(vowels_counter)
