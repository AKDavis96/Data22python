a = lambda x: x + 15
b = lambda x, y: x * y

print(a(10))
print(b(3, 16))

def multiple(n):
    return lambda x: n * x

print(multiple(2)(15))


l_o_t = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]
l_o_t.sort(key= lambda x: x[1])
print(l_o_t)

dict1 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sorted_dict1 = sorted(dict1, key = lambda x: x["color"])
print(sorted_dict1)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

o = list(filter(lambda x: x % 2 == 0, l))
print(o)


