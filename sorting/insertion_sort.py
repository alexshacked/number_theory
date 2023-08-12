import sort_utils as su

def go_alg_cormen_insertion(go_framework):
    """
        driver for cormen version of insertion_sort
    """

    def cb_alg_cormen_insertion(the_seq):
        """
        the driver for sorting
        """
        print('>>>>>> BEFORE:\n{}'.format(the_seq))
        alg_cormen_insertion(the_seq)
        print('>>>>>> AFTER:\n{}'.format(the_seq))

    go_framework(cb_alg_cormen_insertion)

def go_alg_insertion(go_framework):
    """
        driver for insertion_sort
    """

    def cb_alg_insertion(the_seq):
        """
        the driver for sorting
        """
        print('>>>>>> BEFORE:\n{}'.format(the_seq))
        alg_insertion(the_seq)
        print('>>>>>> AFTER:\n{}'.format(the_seq))

    go_framework(cb_alg_insertion)

def alg_cormen_insertion(seq):
    """
    chapter 2 - page 18
    """
    size = len(seq)

    for i in range(1, size):
        entrant = seq[i]

        j = i - 1
        while j > -1:
            if seq[j] <= entrant:
                break
            seq[j + 1] = seq[j]
            j -= 1

        seq[j+1] = entrant

def alg_insertion_insert(seq, j):
    idx = j - 1
    while idx > -1:
        if seq[idx] <= seq[idx + 1]:
            break
        su.swap(seq, idx, idx + 1)
        idx -= 1

def alg_insertion(seq):
    for i in range(1, len(seq)):
        alg_insertion_insert(seq, i)



