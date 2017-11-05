
def is_valid_dna(sequence):
    return all(x in 'ACTG' for x in sequence)


def complement_WC(sequence):
    if not is_valid_dna(sequence):
        print('not a valid sequence')
        return
    trns = ''.maketrans('ATCG', 'TAGC')
    return sequence.translate(trns)


def palindrome_WC(sequence):
    wc_seq = complement_WC(sequence)
    n = len(sequence)
    return all(sequence[i] == wc_seq[n - 1 - i] for i in range(n // 2 + 1))
