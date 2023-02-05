import numpy as np

'''
a. What does this class do?
class MinimalSumOfSquares_Naive exposes an API consisting of functions:
sum_sqrt(), show_sum(). 
sum_sqrt(N) is the main function. For an input parameter N : integer,
the function will return the SMALLEST set of natural numbers that respect
two (2) conditions:
cond. 1: the SUM of numbers in the set equals the input parameter N.
cond. 2: every number in the set has a square which is also a natural number.

b. Why is this class Naive?
It is naive because,  first it finds all the sets of natural numbers that satisfy the 
two(2) conditions and then it takes only the smallest one.
This implementation does not make use of the known theorems from Number Theory
that address the problem of SUM OF SQUARES. For example that any natural number can be
represented by a sum of four (4) squares if not less.
Using this knowledge the implementation could have filtered out many intermediate
results, generating a much faster algorithm.
Specialised classes deriving from MinimalSumOfSquares_Naive will do just that.

c. What can one do? Everyone needs to start as a child before he grows up.
And when he is a child he is naive.
By definition.
'''


class MinimalSumOfSquares_Naive:
    def _squares(n):
        mid = n // 2
        cands = list(np.arange(mid) + 1)
        sqs = [i * i for i in cands if i * i <= n]
        rqs = list(reversed(sqs))
        return rqs

    def _leader_possibilities(self, lead_sqr, rest_sqrs, N):
        results = []

        if lead_sqr <= N:
            leaders = []
            while (np.sum(leaders) + lead_sqr) <= N:
                leaders.append(lead_sqr)

                if np.sum(leaders) == N:
                    results.append(leaders)
                elif len(rest_sqrs) > 1:
                    for i in range( len(rest_sqrs) - 1):
                        sub_res = self._leader_possibilities(rest_sqrs[i], rest_sqrs[i+1:], N - np.sum(leaders))
                        for one_sub_res in sub_res:
                            complete = leaders + one_sub_res
                            results.append(complete)
                else: # len(rest_sqrs)  = 1
                    diff = N - np.sum(leaders)
                    tail = [1]*diff
                    complete = leaders + tail
                    results.append(complete)
        else: # lead_sqr > N : this lead_sqr is bigger than the remaining N. try the next lead square.
            if len(rest_sqrs) > 1:
                for i in range(len(rest_sqrs) - 1):
                    sub_res = self._leader_possibilities(rest_sqrs[i], rest_sqrs[i + 1:], N)
                    results.extend(sub_res)
            else: # len(rest_sqrs)  = 1
                ones = [1]*N
                results.append(ones)

        return results

    def _possibilities(self, sqrs, n):
        all_posbs = []
        for i in range( len(sqrs) ):
            posbs_sets = self._leader_possibilities(sqrs[i], sqrs[i+1:], n)
            all_posbs.extend(posbs_sets)

        return all_posbs

    def sum_sqrt(self, n):
        sqrs = MinimalSumOfSquares_Naive._squares(n)
        poss = self._possibilities(sqrs, n)

        def get_winner_possibility(possibs):
            sorts = {}
            for pos in possibs:
                sorts[len(pos)] = pos
            short = np.min(np.array(list(sorts.keys())))
            return sorts[short]

        winner = get_winner_possibility(poss)
        return winner

    def show_sum(self, sm):
        srs = [str(r) for r in sm]
        msg = '{}:   {}'.format(np.sum(sm), ' '.join(srs))
        print(msg)


def tester(msos,  limit):
    for num in range(2, limit +1):
        res = msos.sum_sqrt(num)
        msos.show_sum(res)


if __name__ == '__main__':
    tester(MinimalSumOfSquares_Naive(), 100)