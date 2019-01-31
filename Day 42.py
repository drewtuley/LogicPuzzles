# insert + and - signs to achieve the totals given:
# 12 3 4 5 6 = 10
# 2 2 3 4 5 = 0
# 7 6 2 5 1 = 7
# 5 4 3 1 4 = 9
# 8 4 5 2 1 = 8

from itertools import permutations

base_set = '++++----'
sums = [(['12', '3', '4', '5', '6'], 10),
        (['2', '2', '3', '4', '5'], 0),
        (['7', '6', '2', '5', '1'], 7),
        (['5', '4', '3', '1', '4'], 9),
        (['8', '4', '5', '2', '1'], 8)]

possibilites = []
for p in permutations(base_set, 4):
    if p not in possibilites:
        possibilites.append(p)

for p in possibilites:
    p = p + ('',)
    # print(p)
    for s in sums:
        test_sum = "".join(["".join(list(z)) for z in zip(s[0], p)])
        if eval(test_sum) == s[1]:
            print('{0}={1}'.format(test_sum, s[1]))
