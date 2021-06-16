a = [2]
b = [1]
num_list = []
even_odd = [0, 0]

def adding(number):
    while len(num_list) <= number:
        num_list.append(1)
    for i in num_list:
        if num_list.index(i) % 2 == 0:
            even_odd[0] += num_list.index(i)
        if num_list.index(i) % 2 != 0:
            even_odd[1] += num_list.index(i)
    return even_odd


print(adding(5))