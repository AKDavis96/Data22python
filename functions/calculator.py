def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1-num2
    elif operator == "/" and num2 != 0:
        return num1/num2
    elif operator == "*":
        return num1*num2
    else:
        print("invalid entry")

print(calculator(8,"+",2))
print(calculator(8,"-",2))
print(calculator(7,"/",0))
print(calculator(8,"*",2))
