

def numbers_multiples(mult1, mult2, end):
    count = 0
    start = 0
    while start < end - 1:
        start += 1
        if start % mult2 == 0 or start % mult1 == 0:
            count = count + start
    print(count)


numbers_multiples(5, 3, 1000)




