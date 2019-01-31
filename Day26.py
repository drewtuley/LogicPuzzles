from itertools import permutations

# Write down a straightforward subtraction sum, A-B=C
# where each of the numbers (A,B and C) are made up of
# nine digits, 1-9 inclusive, with each digit being used
# once only in each number.

# I ran this for several hours without an answer - so it would
# appear to be horrendously inefficient

# The 'well known' answer is:
# 987654321
# 123456789 -
# ---------
# 864197532

# But I also found:
# 912764358
# 456382179 -
# ---------
# 456382179
rng = '987654321'
for ap in permutations(rng, 9):
    a = int("".join(ap))
    for bp in permutations(rng, 9):
        b = int("".join(bp))
        if b < a:
            for cp in permutations(rng, 9):
                c = int("".join(cp))
                if a - b == c:
                    print(a, b, c)
