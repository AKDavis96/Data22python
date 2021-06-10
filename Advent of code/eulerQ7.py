import math

prime_numbers = [2]
not_prime = [1]
y = 3


def is_prime(x):
    for n in range(2, math.floor(x ** 0.5) + 1):
        if x % n == 0:
            return False
    return True


def nth_prime(p):
    y = 3
    while len(prime_numbers) < p:
        if is_prime(y) is True:
            prime_numbers.append(y)
            y += 2
        else:
            not_prime.append(y)
            y += 2
    return prime_numbers[-1]

print(nth_prime(10001))

