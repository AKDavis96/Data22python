list_data = [1, 2, 3, 4, 5]

for num in list_data:
    print(num*2)

embedded_list = [[1,2,3], [4,5,6]]
for data in embedded_list:
    print(data*2)
    for num in data:
        print(num*2)