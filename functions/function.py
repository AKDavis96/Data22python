def print_something():  # just defining here
    print("something")


print_something()  # calling here


def print_anything(print_string: str):
    print("Hi, " + print_string)


print_anything("Aaron")


def addition(num1=1, num2=1):  # the = sign defaults to that number
    return num1 + num2


print(addition(1, 2))


def multi_args(*multiargs):
    print(type(multiargs))
    for arg in multiargs:
        print(arg)


multi_args(1, 2, 1, 2, 3, 4, 5, 3)


def division(num: int, denom: int) -> float:
    return num / denom


print(division(3,4))
