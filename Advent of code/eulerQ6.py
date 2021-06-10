each_square = []
total_square = []
for x in range(1, 101):
    each_square.append(x * x)
es = sum(each_square)
for n in range(1, 101):
    total_square.append(n)
    ts = sum(total_square) * sum(total_square)
print(ts - es)





