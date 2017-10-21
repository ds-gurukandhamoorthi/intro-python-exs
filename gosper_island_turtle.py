import argparse
from Turtle import Turtle
from lindenmayer_turtle import lindenmayer_turtle
from lindenmayer import lindenmayer

def gosper_island(n):
    return lindenmayer('LF--RF--LF--RF--LF--RF', {'L':'+F---F+++F', 'R': '---F-F+F'},n)
# +F---F+++FF--+F---F+++FF--+F---F+++FF--+F---F+++FF--+F---F+++FF--+F---F+++FF

#FIXME:not yet functioning

def gosper_island_iter(n):
    if n < 1:
        return ''
    SINGLE = '--F--F--F++'
    # return SINGLE + '++++' + SINGLE
    if n == 1:
        return SINGLE + SINGLE
    if n == 2:
        res =  SINGLE + '++++' + SINGLE
        res = res + '++++' + res
        res = res + '++++' + res
        return res

def gosper_island_iter_half(n):
    if n < 1:
        return ''
    SINGLE = '--F--F--F++'
    if n == 1:
        return SINGLE 
    if n == 2:
        res =  SINGLE + '++++' + SINGLE
        res = res + '++++' + res
        res = res + '++++' + res
        return res
    
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw Gosper''s Island')
    parser.add_argument('n', type=int, help='order of the Hilbert curve')
    parser.add_argument('step_size', type=float, help='size of the step')
    args = parser.parse_args()
    n = args.n
    step_size = args.step_size
    turt = Turtle(0.5, 0.5, 30)
    # print(gosper_island(n))
    # t = lindenmayer_turtle(gosper_island_iter(n), step_size, turt, angle=30)
    # t = lindenmayer_turtle(gosper_island_iter_half(n), step_size, turt, angle=30)
    strng = '+F---F++F'
    # strng = '----F----F----F'
    t = lindenmayer_turtle(strng, step_size, turt, angle=19.1134)
    t.draw()

