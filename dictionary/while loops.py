x = 0
while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x += 1


age = input("How old are you? ")
while age.isnumeric() is False:
    input("Age must be an integer")
    if age.isnumeric() is not True:
        break
print(f"Your age is {age}")





