from itertools import combinations, permutations

# Using the numbers as shown below (in base_number_pool) construct a 3D cube
# such that each row (x and y) and column adds up to 12 (ignore diagonals)

# DOES NOT WORK YET

base_number_pool = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8]
number_pool1 = []
for c in combinations(base_number_pool, 3):
    if sum(c) == 12:
        for p in permutations(c, 3):
            if p not in number_pool1:
                number_pool1.append(p)
print(len(number_pool1))

number_pool2 = []
for c in combinations(number_pool1, 3):
    if c[0][0] + c[1][0] + c[2][0] == 12 and \
            c[0][1] + c[1][1] + c[2][1] == 12 and \
            c[0][2] + c[1][2] + c[2][2] == 12:
        if c not in number_pool2:
            number_pool2.append(c)

print(len(number_pool2))

for c in combinations(number_pool2, 3):
    nums_used = []
    for x in range(0, 3):
        for y in range(0, 3):
            for z in range(0, 3):
                nums_used.append(c[x][y][z])
    nums_used.sort()
    if nums_used == base_number_pool:
        print(c)
