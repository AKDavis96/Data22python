import numpy as np
import math

data = np.genfromtxt('day1_numbers.txt', delimiter='')
expense_report = data
len(expense_report)
num1 = 0
num2 = 0
num3 = 0
counter_1 = 0
counter_2 = 0

while num1 + num2 != 2020:
    if counter_2 + 1 != len(expense_report):
        counter_2 += 1
    elif counter_2 + 1 == len(expense_report):
        counter_2 = 0
        counter_1 += 1
    if counter_2 == counter_1:
        counter_2 += 1
    num1 = expense_report[counter_1]
    num2 = expense_report[counter_2]
print(num1 * num2)
print(f"{num1} + {num2} = {num1 + num2}")