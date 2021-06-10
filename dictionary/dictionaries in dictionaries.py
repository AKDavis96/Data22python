dict_data = {1: {"name" : "aaron", "money" : "£3.40"}, 2: {"name" : "jon", "money" : "£6.34"}, 3: {"name" : "luke", "money" : "£0.32"}}

dict_data.keys()
for i in dict_data.keys():
    for value in dict_data[i].values():
        print(str(i) + " " +value)
        print(f"{str(i)} {value}")

for item in dict_data.values():
    for var in item.values():
        print(var)



list_numbers = [1, 2, 3, 4, 5]

for num in list_numbers:
    if num == 3:
        print("I found 3!")
    elif num > 3:
        print("gone too far")
    else:
        print("too soon")