def find_duplicate(array):
    array.sort()
    for i in range(len(array)-1):
        if(array[i] == array[i+1]):
            return False
    return True



print(find_duplicate([1,2,3]))
print(find_duplicate([1,2,1]))
