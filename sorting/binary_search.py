import sort_utils as su

def go_lion(go_framework):
    """
    driver for binary_insert
    """
    def cb_lion(the_seq):
        """
        driver for binary insert
        """
        the_seq = sorted(the_seq)
        print("Binary inserting into:\n{}".format(the_seq))
        n = int(input('\nnew element:\n'))
        bigger = binary_insert(the_seq, n)
        print("Element <{}> added:\n{}".format(n, bigger))

    go_framework(cb_lion)


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
