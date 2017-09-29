from gray_code import gray_code
from math import log
import argparse

def beckett_characters(n):
    res = []
    code = gray_code(n)
    stage = set() 
    for val, nxt in zip(code, code[1:]):
        differing_bit = val ^ nxt
        is_entering = differing_bit & nxt > 0
        actor = int(log(differing_bit, 2) + 1)
        if is_entering:
            action = 'enter'
            stage.add(actor)
        else:
            action = 'exit'
            stage.remove(actor)
        res += [(action, actor, list(stage))]
    return res + [('exit', n,[])]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulate Beckett''s characters in the play `Quad`')
    parser.add_argument('nb_characters', type=int, help='number of characters in the play')
    args = parser.parse_args()
    nb_characters = args.nb_characters

    for action, actor, stage in beckett_characters(nb_characters):
        print(  action.rjust(8), actor, stage)
