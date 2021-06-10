a = 2
b = 5.4
c = "How old are you? "
print(c + "I am " + str(a) + str(b)) #converting to strings


int_string = "6"
print(type(int_string)) #converting to int
print(type(int(int_string)))


name = "dog"
years = 7
height_cm = 60.2

print(f"{name} is {years} years old and {height_cm}cm tall") #f string

pi = 3.14159265359
print(f"Pi to 3 decimal places {pi:.3f}")


score = 16
score_max = 26

print(f"You scored {score/score_max}")
print(f"You scored {score/score_max:%}")
print(f"You scored {score/score_max:.2%}")
print(f"You scored {score/score_max:.0%}")


