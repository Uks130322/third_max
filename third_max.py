def third_max(lst: list[int]) -> int:
    """Find third max element of list"""

    first = lst[0]
    second = third = False

    for number in lst:
        if number == first:
            continue
        if number > first:
            first, second, third = number, first, second
        elif not second:
            second = number
        elif number == second:
            continue
        elif not third or number > third:
            third = number
        print(first, second, third)

    if first == second or second == third or second is False or third is False:
        return first
    else:
        return third


print(third_max([0, 1, 3, 2, 5, 7, 9]))
print(third_max([3, 2]))      
print(third_max([3, 3, 4, 3, 4, 3, 0, 3, 3]))
