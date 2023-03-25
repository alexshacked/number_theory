import numpy as np
import sorting as sb


def go_quick_lomuto():
    """
        driver for quick_sort with lomuto_partitioning
    """

    def cb_quick_lomuto(the_seq):
        """
        the driver for sorting
        """
        print('>>>>>> BEFORE:\n{}'.format(the_seq))
        sb.quick_lomuto(the_seq, lo=0, hi=len(the_seq)-1)
        print('>>>>>> AFTER:\n{}'.format(the_seq))

    go_framework(cb_quick_lomuto)

def go_lomuto():
    """
        driver for lomuto_partitioning
    """

    def cb_lomuto(the_seq):
        """
        the driver for sorting
        """
        print('Before:\n{}'.format(the_seq))
        new_pivot_index = sb.lomuto(the_seq, lo=0, hi=len(the_seq)-1)
        print('After:\n{}'.format(the_seq))

    go_framework(cb_lomuto)


def go_quick_partitioning():
    """
    driver for quick_sort_partitioning
    """
    def cb_quick(the_seq):
        """
        the driver for sorting
        """
        print('Before:\n{}'.format(the_seq))
        n = int(input('\nwhat is pivot index?\n'))
        the_seq = sb.quick_sort_partitioning(the_seq, px=n)
        print('After:\n{}'.format(the_seq))

    go_framework(cb_quick)

def go_sort():
    """
    driver for al_sort
    """
    def cb_sort(the_seq):
        """
        the driver for sorting
        """
        print('Before:\n{}'.format(the_seq))
        the_seq = sb.alx_sort(the_seq)
        print('After:\n{}'.format(the_seq))

    go_framework(cb_sort)


def go_lion():
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
        bigger = sb.binary_insert(the_seq, n)
        print("Element <{}> added:\n{}".format(n, bigger))

    go_framework(cb_lion)


def go_framework(fn):
    """
    driver framework
    """
    while True:
        print("\n\n---------------------------------------------")
        n = int(input('how many?:\n'))
        the_seq = np.random.randint(low=1, high=50, size=n).tolist()

        fn(the_seq)

        n = int(input('\nanother run? Enter 0 or 1.\n'))
        if n == 0:
            break

    print('Goodbye.')  # polite


if __name__ == '__main__':
    go_quick_lomuto()