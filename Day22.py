from itertools import permutations
import copy
from datetime import datetime

# Brute solution finder for:
# Using all the numbers from 1 to 25 fill in a 5x5 grid such that all the rows, columns and diagonals
# add up to 65. Start with 1 (one) in the centre tile.

# NB: does not eliminate vertical or horizontal mirror solutions. (so will probably take 4x longer than necessary)
print('start: {}'.format(datetime.now()))
mid_row = [c for c in permutations(range(1, 26), 5) if sum(c) == 65 and c[2] == 1]
for mr in mid_row:
    r = [r for r in range(1, 26)]
    for x in mr:
        r.remove(x)
    vert_mid_row = [c for c in permutations(r, 4) if sum(c) == 64]
    for vr in vert_mid_row:
        r1 = copy.copy(r)
        for v in vr:
            r1.remove(v)
        row1 = [c for c in permutations(r1, 4) if sum(c) == 65 - vr[0]]
        for rr1 in row1:
            r2 = copy.copy(r1)
            for v in rr1:
                r2.remove(v)
            row2 = [c for c in permutations(r2, 4) if sum(c) == 65 - vr[1]]
            for rr2 in row2:
                r3 = copy.copy(r2)
                for v in rr2:
                    r3.remove(v)
                row3 = [c for c in permutations(r3, 4) if sum(c) == 65 - vr[2]]
                for rr3 in row3:
                    r4 = copy.copy(r3)
                    for v in rr3:
                        r4.remove(v)
                    row4 = [c for c in permutations(r4, 4) if sum(c) == 65 - vr[3]]
                    for rr4 in row4:
                        if sum([rr1[0], rr2[0], mr[0], rr3[0], rr4[0]]) == 65 and \
                                sum([rr1[1], rr2[1], mr[1], rr3[1], rr4[1]]) == 65 and \
                                sum([rr1[2], rr2[2], mr[3], rr3[2], rr4[2]]) == 65 and \
                                sum([rr1[3], rr2[3], mr[4], rr3[3], rr4[3]]) == 65 and \
                                sum([rr1[0], rr2[1], mr[2], rr3[2], rr4[3]]) == 65 and \
                                sum([rr1[3], rr2[2], mr[2], rr3[1], rr4[0]]) == 65:
                            print('{6}: {0} {1} {2} {3} {4} {5}'.format(mr, vr, rr1, rr2, rr3, rr4, datetime.now()))
