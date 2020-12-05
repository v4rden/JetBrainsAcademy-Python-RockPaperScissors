x = float(input())
y = float(input())

x_is_positive = x > 0
y_is_positive = y > 0

if x_is_positive and y_is_positive:
    print("I")
elif y_is_positive:
    print("II")
elif not x_is_positive and not y_is_positive:
    print("III")
else:
    print("IV")
