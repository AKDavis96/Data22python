age = input("How old are you? ")
while age.isnumeric() is False:
    age = input("Age must be an integer ")
    if age.isnumeric() is True:
        break
print(f"Your age is {age}")