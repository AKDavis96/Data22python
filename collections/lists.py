shopping_list = ["Bread", "Lettuce", "Potatoes", "Bananas"]
print(type(shopping_list))

print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list[len(shopping_list)-1])

shopping_list[0] = "Sugar"   #change list
print(shopping_list)

shopping_list.append("Carrots")  #add to list
print(shopping_list)

shopping_list.remove("Lettuce") #remove from list
print(shopping_list)

shopping_list.pop()   #removes last item
print(shopping_list)



mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

print(mixture[1:3])
print(mixture[2::2]) #starts at 2 jumping up in 2
print(mixture[2:])
print(mixture[::2])
# [a:b:c] a is start, b is end, c is increment
