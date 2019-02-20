from itertools import permutations
import copy


# Use the following numbers to complete a 4x4 magic square such that all the columns
# and rows add up to 30
# Numbers: 1 2 3 4 5 6 10 11 12 12 13 14
# Initial square:
# x x x x
# x 8 x x
# x x 4 x
# 1 x x x


def copy_except(source, exclusions):
    target = copy.copy(source)
    for e in exclusions:
        target.remove(e)
    return target


def check_columns(r1, r2, r3, r4):
    for col in range(0, 4):
        if r1[col] + r2[col] + r3[col] + r4[col] != 30:
            return False
    return True


number_pool = [1, 1, 2, 3, 4, 4, 5, 6, 8, 10, 11, 12, 12, 13, 14, 14]
solutions = []
for row1 in permutations(number_pool, 4):
    if sum(row1) == 30:
        # print(c)
        number_pool2 = copy_except(number_pool, row1)
        for row2 in permutations(number_pool2, 4):
            if sum(row2) == 30 and row2[1] == 8:
                number_pool3 = copy_except(number_pool2, row2)
                for row3 in permutations(number_pool3, 4):
                    if sum(row3) == 30 and row3[2] == 4:
                        number_pool4 = copy_except(number_pool3, row3)
                        for row4 in permutations(number_pool4, 4):
                            if row4[0] == 1 and check_columns(row1, row2, row3, row4):
                                sol = list(row1) + list(row2) + list(row3) + list(row4)
                                if sol not in solutions:
                                    solutions.append(sol)
                                    print(sol)
