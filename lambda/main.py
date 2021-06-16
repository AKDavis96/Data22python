# def add(num1, num2):
#     return num1 + num2
#
#
# print(add(1, 2))
#
#
# addition = lambda num1, num2: num1 + num2
#
# print(addition(2, 3))

saving = [234.00, 278.00, 327.00, 92.00]

# bonus = list(map(lambda x: x * 1.1, saving))
#
# print(bonus)

bonus= []

for i in saving:
    bonus.append(i * 1.1)

print(bonus)