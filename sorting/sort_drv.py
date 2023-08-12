import numpy as np
import insertion_sort as ins
import quick_sort as qs
import alex_sort as als
import binary_search as bs


def go_framework(fn):
    """
    driver framework
    """
    while True:
        print("\n\n---------------------------------------------")

        the_seq = make_input()

        fn(the_seq)

        n = int(input('\nanother run? Enter 0 or 1.\n'))
        if n == 0:
            break

    print('Goodbye.')  # polite

def make_input():
    n = int(input('how many?:\n'))
    seq = np.random.randint(low=1, high=50, size=n).tolist()
    return seq

if __name__ == '__main__':
    ins.go_alg_cormen_insertion(go_framework)