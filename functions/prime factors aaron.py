import math


def finding_prime_factor(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            n = n / i
        else:
            i = i + 1
    print(n)


finding_prime_factor(49)