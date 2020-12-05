def get_result(coin, cost, animal):
    amount = coin // cost

    if amount < 1:
        return "None"

    result = f"{amount} {animal}"

    if amount != 1 and animal != "sheep":
        result = result.__add__("s")

    return result


coins = int(input())

if coins >= 6769:
    print(get_result(coins, 6769, "sheep"))
elif coins >= 3848:
    print(get_result(coins, 3848, "cow"))
elif coins >= 1296:
    print(get_result(coins, 1296, "pig"))
elif coins >= 678:
    print(get_result(coins, 678, "goat"))
elif coins >= 23:
    print(get_result(coins, 23, "chicken"))
else:
    print("None")
