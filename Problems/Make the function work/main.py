def closest_higher_mod_5(x):
    counter = x
    while counter % 5 != 0:
        counter += 1
    return counter
