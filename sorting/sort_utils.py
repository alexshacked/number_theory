def swap(seq, i, j):
    """
    swap to elements in sequence
    """
    tmp = seq[i]
    seq[i] = seq[j]
    seq[j] = tmp


def log(msg, frame, newl=''):
    """
    log brings identation based on the frame position in the call stack
    """
    idnt = '\t' * frame
    lmsg = newl + idnt + str(msg)
    print(lmsg)


def format_list(l):
    """
    print a sequence keeping elements aligned to the left
    """
    tmpl = '{:<4}'
    strs = [tmpl.format(one) for one in l]
    return ' '.join(strs)


def show_list(l, frame):
    """
    print both the indexes and the elements of a sequence
    """
    l1 = range(len(l))
    log(format_list(l1), frame)
    log(format_list(l), frame)