import argparse

def move(frm, to):
    print(frm+1,'->', to+1)

def zero_prepend(array, size_needed):
    zeros = [0] * (size_needed - len(array))
    return zeros + array[:]


def hanoi_towers(n):
    nums = list(range(1,n+1))
    return [ nums,
            [],
            []]

def hanoi_variant_towers(n):
    nums = list(range(1,n+1))
    odds = [n for n in nums if n % 2 == 1]
    evens =  [n for n in nums if n % 2 == 0]
    return [ odds,
            [],
            evens]

def print_towers(towers):
    height = max([len(tw) for tw in towers])
    towers_ = [zero_prepend(tw, height) for tw in towers]
    for a, b, c in zip(*towers_):
        a = ('*' * a).center(15)
        b = ('*' * b).center(15)
        c = ('*' * c).center(15)
        print(a, b, c)

def animate_sol(towers, sol):
    towers_ = towers[:]
    print_towers(towers_)
    print()
    for step in sol:
        towers_= make_move(towers_, step)
        print(step[0]+1, step[1]+1,sep='->')
        print_towers(towers_)
        print()

def make_move(towers, move):
    towers_ = towers[:]
    frm, to = move
    assert len(towers[frm]) > 0
    disc = towers[frm][0]
    if len(towers[to]) == 0:
        towers_[to] = [disc]
        towers_[frm] = towers[frm][1:]
        return towers_
    disc_there = towers[to][0]
    assert disc_there >= disc
    towers_[to] = [disc] + towers_[to]
    towers_[frm] = towers[frm][1:]
    return towers_
    


def hanoi_steps(start, end, n):
    intermediate = 3-(start+end)
    if n==0:
        return []
    res = []
    res += hanoi_steps(start, intermediate,  n-1)
    res += [(start, end)]
    res += hanoi_steps(intermediate, end,  n-1)
    return res

def hanoi(start, end, intermediate, n):
    if n==0:
        return
    hanoi(start, intermediate, end, n-1)
    move(start, end)
    hanoi(intermediate, end, start, n-1)

def hanoi_(start, end, n):
    hanoi(start, end, 3-(start+end), n)

#here hanoi is synonym of move n ordered pile from, to with an empty stack

def pile(from1, pile_on, k):
    from2 = 3-(pile_on + from1)
    if k == 0:
        return []
    if k == 1:
        return [(from1, pile_on)]
    if k == 2:
        return [(from2, pile_on),
                (from1, pile_on)]

def merge(from1, to, k):
    from2 = 3-(pile_on + from1)
    if k == 0:
        return []




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solver tower of Hanoi problem')
    parser.add_argument('nb_discs', type=int, help='number of discs')
    args = parser.parse_args()
    nb_discs = args.nb_discs
    # hanoi_(0,2,nb_discs)
    # hanoi_variant(0,2,1,nb_discs)
    print(hanoi_variant_towers(nb_discs))

    # ordinary = hanoi_towers(3)
    # sol = hanoi_steps(0,2,3)
    # animate_sol(ordinary, sol)

    towers = hanoi_variant_towers(nb_discs)
    print_towers(towers)
    piling = pile(0,1,2)
    print("piling", piling)
    animate_sol(towers,piling)
