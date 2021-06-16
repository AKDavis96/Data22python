num_list = []
even_odd = [0, 0]

def adding(number):
    counter = 0
    while len(num_list) <= number:
        num_list.append(counter)
        counter += 1
    for i in num_list:
        if i % 2 == 0:
            even_odd[0] += i
        if i % 2 != 0:
            even_odd[1] += i
    return even_odd


print(adding(5))