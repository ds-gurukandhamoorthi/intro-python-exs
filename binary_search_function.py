def compare_function(func, x0, tolerance, est):
    "Tells if a given function evaluates to ext at x0 with the given tolerance: f(x0) = est ? Is the estimate greater than the actual value?"
    val = func(x0)
    if abs(val-est) < tolerance:
        return 0
    if est > val:
        return 1
    return -1

def binary_search_interval(lo, hi, func, y, tolerance = 10**-5, cmp_func = compare_function):
    midpoint = (lo + hi) / 2
    res_comp = cmp_func(func, midpoint, tolerance, y)
    if res_comp == 0:
        return midpoint
    if res_comp > 0:
        return binary_search_interval(midpoint, hi, func, y)
    return binary_search_interval(lo, midpoint,  func, y)

def inverse(func, y, lo, hi, tolerance = 10**-5):
    return binary_search_interval(lo, hi, func, y)

