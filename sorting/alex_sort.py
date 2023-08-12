import sort_utils as su
import binary_search as bs

def go_sort(go_framework):
    """
    driver for al_sort
    """
    def cb_sort(the_seq):
        """
        the driver for sorting
        """
        print('Before:\n{}'.format(the_seq))
        the_seq = alx_sort(the_seq)
        print('After:\n')
        su.show_list(the_seq, 0)

    go_framework(cb_sort)

def alx_sort(seq):
    """
    sort algorithm - recursively generate sorted pairs, then binary-insert.
    """
    if len(seq) < 2:
        return seq

    if len(seq) == 2:
        return sort_pair(seq)

    the_sp = sort_pair(seq[:2])
    the_sr = alx_sort(seq[2:])

    res = merge(the_sp, the_sr)
    return res


def merge(sp, sr):
    """
    merging sorted pair into sorted sequence
    """
    if sp[1] <= sr[0]:
        return sp + sr
    elif sp[0] >= sr[-1]:
        return sr + sp

    sr1 = bs.binary_insert(sr, sp[0])
    sr2 = bs.binary_insert(sr1, sp[1])
    return sr2


def sort_pair(pr):
    """
    sort a pair of numbers
    """
    res = pr if pr[0] <= pr[1] else [pr[1], pr[0]]
    return res