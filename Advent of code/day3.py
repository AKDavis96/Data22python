list = [str(x.strip()) for x in open("day3_details.txt", "r").readlines()]

def finding_trees(r, d):
    trees = 0
    a = 0
    b = 0
    row = len(list[0])
    c = len(list) - 1

    while a != c:
        a += d
        if b > row - (r + 1):
            b -= row
            b += r
        elif b <= row - (r + 1):
            b += r
        if list[a][b] == "#":
            trees += 1
    return trees

finding_trees(1,1)
print(finding_trees(3,1))
finding_trees(5,1)
finding_trees(7,1)
finding_trees(1,2)

print(finding_trees(1, 1) * finding_trees(3, 1) * finding_trees(5, 1) * finding_trees(7, 1) * finding_trees(1, 2))

