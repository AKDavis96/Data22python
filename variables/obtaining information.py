name = input("Hello, what is your name?  ")
name = name.strip().capitalize()
age = input("Hi " +name +",how old are you? ")
age = str(age)
print("You are " + age + " and your name is " + name +", You will be " + str(int(age)+1) + " on your next birthday!")
print(f"You are {age} and your name is {name}, You will be {int(age)+1} on your next birthday!")

birth_month = input("Which month were you born in? ")
birth_date = input("Which date were you born on? ")
if int(birth_date) == 12 or 11 or 13:
    print(f"Your birthday is on {birth_date}th {birth_month}")
elif int(birth_date) % 10 == 2:
    print(f"Your birthday is on {birth_date}nd {birth_month}")
