
def sum_of_fibonacci(div, limit, term1, term2):  #put which number you want the numbers to be divided by for div
    a = term1
    b = term2
    c = 0
    count = 0
    while a < limit:
        c = a + b
        a = b
        b = c
        if a % div == 0:
            count = count + a
    print(count)


sum_of_fibonacci(2, 4000000, 1, 2)





