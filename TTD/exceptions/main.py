try:
    file = open("order.txt")
    x = 4 / 0
except FileNotFoundError as errmsg:
    print("No File!!!")
    print(errmsg)
except ZeroDivisionError as errmsg:
    print("can't divide by 0!!!")
    print(errmsg)
    raise


