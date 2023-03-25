import sort_utils as su

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

def binary_insert(sr, one):
    """
    lion in the desert
    """
    END = len(sr) - 1
    left = 0
    right = END

    while True:
        ix_mid = (left + right) // 2

        val_mid_minus = sr[ix_mid - 1] if ix_mid > 0 else None
        val_mid = sr[ix_mid]
        val_mid_plus = sr[ix_mid  + 1] if ix_mid < END else None

        if ix_mid == 0 and one <= val_mid:
            return [one] + sr
        elif ix_mid == END and one >= val_mid:
            return sr + [one]
        elif val_mid <= one <= val_mid_plus:
            return sr[:ix_mid + 1] + [one] + sr[ix_mid + 1:]
        elif val_mid_minus <= one <= val_mid:
            return sr[:ix_mid] + [one] + sr[ix_mid:]
        elif one > val_mid_plus:
            left = ix_mid + 1
        else:
            right = ix_mid


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

    sr1 = binary_insert(sr, sp[0])
    sr2 = binary_insert(sr1, sp[1])
    return sr2


def sort_pair(pr):
    """
    sort a pair of numbers
    """
    res = pr if pr[0] <= pr[1] else [pr[1], pr[0]]
    return res
