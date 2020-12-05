initial_sum = float(input())
counter = 0

while initial_sum < 700000:
    counter += 1
    initial_sum += initial_sum / 100 * 7.1

print(counter)
