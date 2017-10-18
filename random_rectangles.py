from Rectangle import Rectangle
import argparse
import random
import matplotlib.pyplot as plt
from itertools import combinations

def rnd(lo, hi):
    return random.random() * (hi-lo) + lo

def random_rectangles(n, lo, hi):
    res = [None] * n
    for i in range(n):
        res[i] = Rectangle(random.random(), random.random(), rnd(lo,hi), rnd(lo,hi))
    return res

def draw_rectangles(lst_rects):
    fig, ax = plt.subplots()
    ax.axis('equal')
    for rect in lst_rects:
        ax.add_patch(rect.get_patch())
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    fig.savefig('tes.png')
    plt.show()

def avg_area(lst_rects):
    return sum([rect.area() for rect in lst_rects])/ len(lst_rects)

def avg_perimeter(lst_rects):
    return sum([rect.perimeter() for rect in lst_rects])/ len(lst_rects)

def avg_inclusions(lst_rects):
    n = len(lst_rects)
    nb_inclus = 0
    nb_pairs = 0
    for i, j in combinations(range(n), 2):
        nb_pairs += 2
        r1, r2 = lst_rects[i], lst_rects[j]
        if r1.contains(r2):
            print(r1, 'contains', r2)
            nb_inclus += 1
        if r2.contains(r1):
            nb_inclus += 1
    return nb_inclus/nb_pairs

def avg_intersections(lst_rects):
    n = len(lst_rects)
    nb_inters = 0
    nb_pairs = 0
    for i, j in combinations(range(n), 2):
        nb_pairs += 1
        if lst_rects[i].intersects(lst_rects[j]):
            nb_inters += 1
    return nb_inters/nb_pairs


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw random rectangles on the unit square')
    parser.add_argument('n', type=int, help='number of rectangles')
    parser.add_argument('lo', type=float, help='lower bound')
    parser.add_argument('hi', type=float, help='higher bound')
    args = parser.parse_args()
    n = args.n
    lo = args.lo
    hi = args.hi

    lst_rects = random_rectangles(n, lo, hi)
    draw_rectangles(lst_rects)
    print('average area', avg_area(lst_rects))
    print('average perimeter', avg_perimeter(lst_rects))
    print('average intersects', avg_intersections(lst_rects))
    print('average inclusions', avg_inclusions(lst_rects))


