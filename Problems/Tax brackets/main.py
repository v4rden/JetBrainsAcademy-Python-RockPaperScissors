income = int(input())
percent = 28

if income < 132407:
    percent = 25
if income < 42708:
    percent = 15
if income < 15528:
    percent = 0

calculated_tax = int(round(income / 100 * percent))
result = f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!'

print(result)
