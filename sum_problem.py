import argparse

def split_of_len(string, array):
    n = len(string)
    m = sum(array)
    assert m == n

    tot = 0
    res = []
    for val in array:
        res += [string[tot:tot+val]]
        tot += val
    return res

def split_and_sum(string, array):
    return sum( [int(n) for n in split_of_len(string, array)])

def gen_possible_subsets(total, max_digits):
    # return [[4,4,2],[4,3,3],[3,3,4]]
    res = []
    for i in range(1, max_digits+1):
        res += gen_set_nums_of_sum(total, i)
    return res

def gen_set_nums_of_sum(total, set_length):
    if set_length == 0 or total < set_length:
        return []
    if total == 1 or set_length == 1:
        return [[total]]
    res = []
    for i in range(1, total):
        for set_ in gen_set_nums_of_sum(total-i, set_length -1):
            res += [[i] + set_]
    return res



def format_solution(string, array):
    return '+'.join( split_of_len(string, array))


def solve_sum_problem(string, total):
    "Given a string 2344056348 inserts + in the right place to get the total (ex: 6987)"
    res = []
    def nb_digits(n):
        return len(str(n))
    # for sum_subset in gen_possible_subsets(len(string), nb_digits(total)):
    for sum_subset in gen_possible_subsets(len(string), len(string)):
        if split_and_sum(string, sum_subset) == total:
            # print('solution', format_solution(string, sum_subset))
            res += [sum_subset]
    return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solve the sum problem')
    parser.add_argument('string', metavar='nums_lhs', help='string to split into numbers with the + sign appropriately: ex: 2344056348')
    parser.add_argument('total', type=int, help='total of the numbers: ex: 6987')
    args = parser.parse_args()

    string = args.string
    total = args.total
    res = solve_sum_problem(string, total)
    for sol in res:
        print(format_solution(string, sol), '=', total)


   # 512 = len(sum_problem.gen_possible_subsets(10,10))
