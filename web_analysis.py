import argparse
from ioutils import read_strings
from wordcount import words
import shelve
TRANS_MATR_KEY='trans_matr_key'
from arrayUtils import group2




def as_tuples(strs):
    res = []
    for line in strs:
        page_nos = [int(x) for x in words(line)]
        for link in group2(page_nos):
            res += [link]
    return res

def link_counts(n, links):
    lnk_cnt = [[0]*n for i in range(n)]
    for from_page, to_page in links:
        lnk_cnt[from_page][to_page] += 1
    return lnk_cnt

def degrees_vec(matr):
    return [sum(row) for row in matr]

def loop_equi_probab(n, p):
    return [[p/n]*n for i in range(n)]

def as_probab(array, p):
    return [ x/sum(array)*p  for x in array]

def link_probab(matr, p):
    res = []
    for row in matr:
        if sum(row) > 1 :
            res += [as_probab(row, p)]
        else:
            res += [[ p / len(row)] * len(row)]
    return res

def transition_matrix(n, links, loop_prob):
    lnk_cnt = link_counts(n, links)
    loop_prob_matr = loop_equi_probab(n, loop_prob)
    otherpage_prob_matr = link_probab(lnk_cnts, 1 - loop_prob)
    return add_matrixes(loop_prob_matr, otherpage_prob_matr)

def add_lists( lsta, lstb):
    return [ a+b for a, b in zip(lsta, lstb)]

def add_matrixes(mata, matb):
    return [ add_lists(lsta, lstb) for lsta, lstb in zip(mata, matb)]

def normalize(array):
    return [x / sum(array) for x in array]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='generate transition matrix given in stdin')
    parser.add_argument('move_to_other_page_prob', type=float, help='the probality for moving to another page through link instead of staying on the same page')
    parser.add_argument('--ignore-multiple-links',  help='if multiple links present (from one to anotgher) ignore them', action='store_true')
    args = parser.parse_args()
    LOOP_PROBAB = 1- args.move_to_other_page_prob
    TRANS_PROB = args.move_to_other_page_prob
    inp = read_strings()
    n = int(inp[0])
    links=as_tuples(inp[1:])
    if args.ignore_multiple_links:
        links=list(set(links)) #unique

    lnk_cnts = link_counts(n, links)
    # print(lnk_cnts)
    # print(degrees_vec(lnk_cnts))
    # print(loop_equi_probab(5,LOOP_PROBAB))
    # print(link_probab(lnk_cnts,TRANS_PROB))
    trns_matr = transition_matrix(n, links, LOOP_PROBAB)
    trns_matr = [normalize(row) for row in trns_matr]

    print(trns_matr)

    

    d = shelve.open('transmatrfile')
    d[TRANS_MATR_KEY] = trns_matr
    d.close()

    dotfile = open('links.dot','w')
    print('digraph Links{', file=dotfile)
    for link in links:
        from_page, to_page = link
        print(from_page, ' -> ', to_page, ';' ,file = dotfile)

    print('}', file=dotfile)
    dotfile.close()
