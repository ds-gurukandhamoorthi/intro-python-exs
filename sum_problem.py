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

def gen_possible_subsets(total):
    #FIXME
    # return [[4,4,2],[4,3,3],[3,3,4]]

def format_solution(string, array):
 ]   return '+'.join( split_of_len(string, array))


def solve_sum_problem(string, total):
    "Given a string 2344056348 inserts + in the right place to get the total (ex: 6987)"
    for sum_subset in gen_possible_subsets(len(string)):
        print(sum_subset)
        if split_and_sum(string, sum_subset) == total:
            print('solution', format_solution(string, sum_subset))
            return sum_subset
    print("solution not found")

if __name__ == "__main__":
    print(split_of_len("2344056348",[4,4,2]))
    print(split_and_sum("2344056348",[4,4,2]))
    print(solve_sum_problem("2344056348",6987))




