def check_palindrome(word):
    length = len(word)

    for i in range(0, length // 2, 1):
        if word[i] != word[length - 1 - i]:
            return "Not palindrome"

    return "Palindrome"


user_input = input()
print(check_palindrome(user_input))
