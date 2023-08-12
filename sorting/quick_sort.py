import sort_utils as su

def go_quick_hoare(go_framework):
    """
        driver for quick_sort with hoare_original__partitioning
    """

    def cb_quick_hoare(the_seq):
        """
        the driver for sorting
        """
        print('>>>>>> BEFORE:\n{}'.format(the_seq))
        quick_hoare(the_seq, lo=0, hi=len(the_seq)-1)
        print('>>>>>> AFTER:\n{}'.format(the_seq))

    go_framework(cb_quick_hoare)

def go_hoare_original(go_framework):
    """
        driver for hoare_partitioning
        from pseudocode in wikipedia page
        not working
    """

    def cb_hoare_original(the_seq):
        """
        the driver for sorting
        """
        print('\nBefore:\n{}\n'.format(the_seq))
        new_pivot_index = hoare_original(the_seq, lo=0, hi=len(the_seq)-1)
        print('After:')
        su.show_list(the_seq, 0)
        print('New pivot: {}'.format(new_pivot_index))

    go_framework(cb_hoare_original)


def go_hoare(go_framework):
    """
        driver for hoare_partitioning
    """

    def cb_hoare(the_seq):
        """
        the driver for sorting
        """
        print('\nBefore:\n{}\n'.format(the_seq))
        new_pivot_index = hoare(the_seq, lo=0, hi=len(the_seq)-1)
        print('After:')
        su.show_list(the_seq, 0)
        print('New pivot: {}'.format(new_pivot_index))

    go_framework(cb_hoare)


def go_quick_lomuto(go_framework):
    """
        driver for quick_sort with lomuto_partitioning
    """

    def cb_quick_lomuto(the_seq):
        """
        the driver for sorting
        """
        print('>>>>>> BEFORE:\n{}'.format(the_seq))
        quick_lomuto(the_seq, lo=0, hi=len(the_seq)-1)
        print('>>>>>> AFTER:\n{}'.format(the_seq))

    go_framework(cb_quick_lomuto)

def go_lomuto(go_framework):
    """
        driver for lomuto_partitioning
    """

    def cb_lomuto(the_seq):
        """
        the driver for sorting
        """
        print('Before:\n{}'.format(the_seq))
        new_pivot_index = lomuto(the_seq, lo=0, hi=len(the_seq)-1)
        print('After:\n{}'.format(the_seq))

    go_framework(cb_lomuto)


def go_quick_partitioning(go_framework):
    """
    driver for quick_sort_partitioning
    """
    def cb_quick(the_seq):
        """
        the driver for sorting
        """
        print('Before:\n{}'.format(the_seq))
        n = int(input('\nwhat is pivot index?\n'))
        the_seq = quick_sort_partitioning(the_seq, px=n)
        print('After:\n{}'.format(the_seq))

    go_framework(cb_quick)


def quick_hoare(seq, lo, hi, frame=0):
    """
    quick_sort with hoare partitioning
    """
    frame += 1
    su.log(
        "######## frame {} ##########################".format(frame),
        frame, '\n'
    )
    su.show_list(seq, frame)
    su.log('{},  {}'.format(lo, hi), frame)
    if lo >= hi or lo == -1:
        su.log('No processing', frame)
        return

    piv = hoare_original(seq, lo, hi)
    su.log("-----------------", frame)
    su.log(piv, frame)
    su.show_list(seq, frame)

    su.log(
        'frame {}. start first recursive quick_hoare. lo: {}, hi: {}'
        .format(frame, lo, piv), # hoare original requires piv
        frame,
        '\n'
    )
    quick_hoare(seq, lo, piv, frame)
    su.log(
        'frame {}. end first recursive quick_hoare. lo: {}, hi: {}'
        .format(frame, lo, piv),
        frame,
        '\n'
    )

    su.log(
        'frame {}. start second recursive quick_hoare. lo: {}, hi: {}'
        .format(frame, piv+1, hi),
        frame,
        '\n'
    )
    quick_hoare(seq, piv+1, hi, frame)
    su.log(
        'frame {}. end second recursive quick_hoare. lo: {}, hi: {}'
        .format(frame, piv + 1, hi),
        frame,
        '\n'
    )


def hoare_original(seq, lo, hi):
    """
    hoare partitioning
    """
    ix_piv = lo + (hi - lo) // 2
    piv = seq[ix_piv]

    su.show_list(seq, 0)
    su.log('lo: {},  high: {}'.format(lo, hi), 0)
    su.log('ix_piv: {}, piv: {}\n'.format(ix_piv, piv), 0)

    i, j = lo - 1, hi + 1
    while True:
        i += 1
        while seq[i] < piv:
            i += 1

        j -= 1
        while seq[j] > piv:
            j -= 1

        su.log('Finished moving indexes. i: {},  j: {}\n'.format(i, j), 0)

        if i >= j:
            return j

        su.swap(seq, i, j)

        su.show_list(seq, 0)
        su.log('lo: {},  high: {}'.format(lo, hi), 0)
        su.log('ix_piv: {}, piv: {}'.format(ix_piv, piv), 0)
        su.log('i: {},  j: {}\n'.format(i, j), 0)


def hoare(seq, lo, hi, frame):
    """
    hoare partitioning
    """
    ix_piv = lo + (hi - lo) // 2
    piv = seq[ix_piv]

    su.show_list(seq, 0)
    su.log('lo: {},  high: {}'.format(lo, hi), 0)
    su.log('ix_piv: {}, piv: {}\n'.format(ix_piv, piv), 0)

    def idx_up(ix, ix_pv):
        rx = ix + 2 if ix_pv - ix == 1 else ix + 1
        return rx

    def idx_down(ix, ix_pv):
        rx = ix - 2 if ix - ix_pv == 1 else ix - 1
        return rx

    i, j = lo - 1, hi + 1
    while True:
        i = idx_up(i, ix_piv)
        while seq[i] < piv and i < hi:
            i = idx_up(i, ix_piv)

        j = idx_down(j, ix_piv)
        while seq[j] > piv and j > 0:
            j = idx_down(j, ix_piv)

        if i >= j:
            if seq[i] > piv and i > ix_piv:
                su.swap(seq, i-1, ix_piv)
                new_piv = i - 1
            elif seq[i] < piv and i < ix_piv:
                su.swap(seq, i + 1, ix_piv)
                new_piv = i + 1
            else:
                su.swap(seq, i, ix_piv)
                new_piv = i

            return new_piv

        su.swap(seq, i, j)

        su.show_list(seq, 0)
        su.log('lo: {},  high: {}'.format(lo, hi), 0)
        su.log('ix_piv: {}, piv: {}'.format(ix_piv, piv), 0)
        su.log('i: {},  j: {}\n'.format(i, j), 0)


def quick_lomuto(seq, lo, hi, frame=0):
    """
    quick_sort with lomuto partitioning
    """
    frame += 1
    su.log(
        "######## frame {} ##########################".format(frame),
        frame, '\n'
    )
    su.show_list(seq, frame)
    su.log('{},  {}'.format(lo, hi), frame)
    if lo >= hi or lo == -1:
        su.log('No processing', frame)
        return

    piv = lomuto(seq, lo, hi)
    su.log("-----------------", frame)
    su.log(piv, frame)
    su.show_list(seq, frame)

    su.log(
        'frame {}. start first quick_lomuto. lo: {}, hi: {}'
        .format(frame, lo, piv-1),
        frame,
        '\n'
    )
    quick_lomuto(seq, lo, piv-1, frame)
    su.log(
        'frame {}. end first quick_lomuto. lo: {}, hi: {}'
        .format(frame, lo, piv - 1),
        frame,
        '\n'
    )

    su.log(
        'frame {}. start second quick_lomuto. lo: {}, hi: {}'
        .format(frame, piv+1, hi),
        frame,
        '\n'
    )
    quick_lomuto(seq, piv+1, hi, frame)

    su.log(
        'frame {}. end second quick_lomuto. lo: {}, hi: {}'
        .format(frame, piv + 1, hi),
        frame,
        '\n'
    )


def lomuto(seq, lo, hi):
    """
    lomuto partitioning
    """
    # hi is the index of the pivot
    i = lo - 1
    for j in range(lo, hi):
        if seq[j] <= seq[hi]:
            i += 1
            su.swap(seq, i, j)
    i += 1
    su.swap(seq, i, hi)
    return i

def quick_sort_partitioning(seq, px):
    """
    my primitive algorithm for partitioning
    """
    size = len(seq)
    left, right = 0,  px + 1

    while not (
        left == (px-1) and right == (size-1) and \
        (seq[left] <= seq[px] <= seq[right])
    ):

        if seq[left] > seq[px] > seq[right]:
            su.swap(seq, left, right)
        elif (left + 1) == px and seq[right] < seq[px]:
            after_piv = px + 1
            su.swap(seq, px, right)
            su.swap(seq, after_piv, right)
            left = px
            px = after_piv
        elif (right + 1) == size and seq[left] > seq[px]:
            before_piv = px -1
            su.swap(seq, px, left)
            su.swap(seq, before_piv, left)
            px = before_piv

        if seq[left] <= seq[px]:
            left = left + 1 if (left + 1) < px else (px - 1)
        if seq[right] >= seq[px]:
            right = right + 1 if (right + 1) < size else size - 1

        print(seq)

    return seq
