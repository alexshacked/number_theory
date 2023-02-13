import numpy as np
import pandas as pd


class Caesar:
    '''
    Decodes a message that was encoded using Caesar Cipher.
    It displays the  whole set of possible decodings coresponding
    to all posibble caesar shifts.
    A human input is required in order to establish which caesar
    shift generates a logical decoded message
    '''
    def __init__(self):
        self.NUM_LETTERS = (ord('z') - ord('a')) + 1

    def __inc(self, ch, delta):
        if ch == ' ':
            return ch
        norm = ord(ch) - ord('a')
        norm1 = (norm + delta) % self.NUM_LETTERS
        rd1 = ord('a') + norm1
        ch1 = chr(rd1)
        return ch1

    def show_ascii_points(self):
        s = ord('a')
        e = s + self.NUM_LETTERS
        points = np.arange(s, e)
        ltrs = [chr(p) for p in points]
        prs = zip(points, ltrs)

        print('############################')
        print('The ascii code points:')
        for pr in prs:
            print(pr)

    def decode(self, encoded):
        print('########################')
        print('Encoded message: {}\n'.format(encoded))
        dec_vals = []

        # go over all  possible caesar shifts
        for i in range(self.NUM_LETTERS):
            lst = [self.__inc(ch, i) for ch in encoded]
            decoded = ''.join(lst)
            dec_vals.append(decoded)

        tbl = pd.DataFrame({'decoded_msg': dec_vals})
        tbl.index.name = 'caesar_shift'
        print(tbl)


if __name__ == '__main__':
    input = 'es tnjui'

    caesar = Caesar()
    # caesar.show_ascii_points()
    caesar.decode(input)


