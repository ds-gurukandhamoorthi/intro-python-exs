from itertools import groupby

def indexRunLength(array):
    "Sort of RunLengthEncoding returning not values but index"
    loc, count = 0, 1
    res = []
    for i in range(1,len(array)):
        if array[i] == array[loc]:
            count = count + 1
        else:
            res += [(loc,count)]
            loc, count = i, 1
    res+=[(loc,count)]
    return res

def indexRunLength2(array):
    loc = 0
    res = []
    for k, g in groupby(array):
        count = len(list(g))
        res += [(loc,count)]
        loc += count
    return res


def rleAndIndex(array):
    "Run Length Encoding Along with the first index of elements"
    loc = 0
    res = []
    for k, g in groupby(array):
        count = len(list(g))
        res += [(count,k,loc)]
        loc += count
    return res




def rle(array):
    "Calculates run length encoding"
    res = []
    for k, g in groupby(array):
        res += [(len(list(g)),k)]
    return res



if __name__ == "__main__":
    five = ['a']*5
    print(indexRunLength([1,2,3,4,5])) 
    print(indexRunLength([1,1,3,4,3])) 
    print(indexRunLength([1,1,3,4,4])) 
    print(indexRunLength2([1,1,3,4,4])) 
    print(rleAndIndex([1,1,3,4,4])) 
    print(rle([1,1,3,4,4])) 
    print(rleAndIndex(five))
    print(rle(five))
