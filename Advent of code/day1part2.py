import numpy as np

data = np.genfromtxt('day1_numbers.txt', delimiter='')
expense_report = data
len(expense_report)


def part_2():
    for num1 in expense_report:
        for num2 in expense_report:
            if (2020 - num1 - num2) in expense_report:
                return num1 * (2020 - num1 - num2) * num2


def part_1():
    for num in expense_report:
        if (2020 - num) in expense_report:
            return num * (2020 - num)


print(part_1())
print(part_2())
