def smallest_number_divisable(num):
    x = 1
    n = num

    while x < num:
        if n % x == 0:
            x += 1
        elif n % x != 0:
            x = 1
            n += num
    return int(n)


print(smallest_number_divisable(20))

