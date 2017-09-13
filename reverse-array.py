a = [1.0,2.0,3.0,4.0,5.0,6.0,7.0]
def reverse(array):
    n = len(array)
    for i in range(n//2):
        array[i], array[n-1-i] = array[n-1-i], array[i]
    return array

print(reverse(a))
