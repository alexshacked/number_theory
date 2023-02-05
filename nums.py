import numpy as np
import itertools
# ver1
# returns the permutations instead of limiting itself to the number of permutations
# by displaying the permutation themselves it is easier to validate and debug the algorithm
# future versions will return the number of permutations as requested
def sums(n):
    the_inp = [n]
    res = [
        the_inp
    ]
    keep_prev_res = {}

    def do_sum(n1, inc, kpr):
        res1 = []

        residual = n1 - inc
        res1.append([inc, residual])

        if residual > inc:
            res2 = []
            for i in range(1,inc+1):
                if i <= residual // 2:
                    if (residual, i) in kpr:
                        dos_res = kpr[(residual, i)]
                    else:
                        dos_res = do_sum(residual, i, kpr)
                        kpr[(residual, i)] = dos_res
                    res2.extend(dos_res)
            res3 = []
            for r in res2:
                if np.max(r) >= inc:
                    res3.append([inc] + r)
            res1.extend(res3)

        return res1

    for i in range(1, n//2 + 1):
        res.extend(do_sum(n, i, keep_prev_res))

    return res

def show_sums(perms):
    res = {}
    for p in perms:
        mx = np.max(p)
        if not mx in res:
            res[mx] = []
        res[mx].append(p)
    ks = sorted(res.keys())
    for k in ks:
        print(k)
        for p in res[k]:
            sp = [str(n) for n in p]
            print('\t' + ' '.join(sp))

### mine
permutations = sums(7)
show_sums(permutations)

### theirs
def func2(n):
    iterable = range(1, n + 1)
    for length in reversed(iterable):
        combinations = itertools.combinations_with_replacement(iterable, length)
        array = np.array(list(combinations))
        mask = np.equal(array.sum(axis=1), n)
        yield from array[mask].tolist()
# for result in func2(15):
#     print(result)