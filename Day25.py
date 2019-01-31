from itertools import permutations

# arrange the digits 1-9 to form:
# a three-digit multiple of 3, a three-digit multiple of 4
# and a three-digit multiple of 5

nums = [x for x in range(1, 10)]
answer=1
for perms in permutations(nums, 9):
    a = int("".join(map(str, perms[0:3])))
    b = int("".join(map(str, perms[3:6])))
    c = int("".join(map(str, perms[6:])))
    if a % 3 == 0 and b % 4 == 0 and c % 5 == 0:
        print(answer, a, b, c)
        answer += 1
# it turns out that there are 3,456 correct permutations, so plenty to choose from
