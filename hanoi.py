import argparse
def move(frm, to):
    print(frm+1,'->', to+1)

def hanoi(start, end, intermediate, n):
    if n==1:
       move(start,end) 
       return
    hanoi(start, intermediate, end, n-1)
    move(start, end)
    hanoi(intermediate, end, start, n-1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solver tower of Hanoi problem')
    parser.add_argument('nb_discs', type=int, help='number of discs')
    args = parser.parse_args()
    nb_discs = args.nb_discs
    hanoi(0,2,1,nb_discs)



