#lists with no duplicates
car_parts = {"wheels", "doors", "exhaust", "exhaust"}
print(car_parts)

car_parts_l = ["wheels", "doors", "exhaust", "exhaust"]
print(set(car_parts_l))

car_parts.add("windows")  #adding to a set
print(car_parts)

x = frozenset([1,2,3,4])
print(x)

a = [1, 2, 2, 3, 3]

print(len(a) - len(set(a)))
