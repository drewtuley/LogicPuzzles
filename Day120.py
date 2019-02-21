# Given 2.2.2.2.2.2=?
# use the mathematical symbols + - * / such that ?=4
# using the same signs so that ?=2 - how many solutions are there

symbols = ['+', '-', '*', '/']


def sym_permutations():
    for s1 in symbols:
        for s2 in symbols:
            for s3 in symbols:
                for s4 in symbols:
                    for s5 in symbols:
                        yield (s1 + s2 + s3 + s4 + s5)


for syms in sym_permutations():
    base_sum = ''.join([''.join(list(x)) for x in zip('222222', syms + '=')])
    eq4 = base_sum + '=4'
    eq2 = base_sum + '=2'
    if eval(eq4):
        print(eq4)
    if eval(eq2):
        print(eq2)
