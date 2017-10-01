import random

def random_array(n):
    arr = list(range(n))
    return random.sample(arr, n)

def find_max(array, k):
    "find the maximum of first k elements"
    max_at = 0
    maxi = array[0]
    for i in range(1,k):
        elem = array[i]
        if elem > array[max_at]:
            max_at, maxi = i, elem
    return max_at

def flip_in_place(array, k):
    "Reverse (in place) first k elements in the array"
    assert len(array) >= k
    for i in range(k//2):
        array[i], array[k-1-i] = array[k-1-i],array[i]




def pancake_sort(array):
    def largest_to_end(nb):
        i = find_max(array, nb)
        flip_in_place(array, i+1)
        flip_in_place(array, nb)
    for i in reversed(range(2,len(array)+1)):
        largest_to_end(i)




if __name__ == "__main__":
    a =random_array(10)
    print(a)
    pancake_sort(a)
    print(a)
    

    
