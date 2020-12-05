def count_desks(students):
    return int(students / 2 + 0.5)


first_group = int(input())
second_group = int(input())
third_group = int(input())

sum_desks = count_desks(first_group) + count_desks(second_group) + count_desks(third_group)
print(sum_desks)
