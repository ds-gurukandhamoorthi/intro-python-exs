import argparse
def odd(n):
    return n%2 != 0

def nb_true_values(array):
    return sum([ x == 'True' for x in array])

def odd_number_of_truths(array):
    return odd(nb_true_values(array)) 

def majority_truths(array):
    return nb_true_values(array) > len(array)/2


parser = argparse.ArgumentParser(description='Says if the number of True elements is odd')
parser.add_argument('truths', help='True/False',choices=['True','False'], nargs='+')
parser.add_argument('--majority', dest='apply_func', default=odd_number_of_truths, const=majority_truths, action='store_const')
args = parser.parse_args()

apply_func = args.apply_func
print(apply_func(args.truths))

