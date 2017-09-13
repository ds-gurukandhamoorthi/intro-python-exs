
def isPowerOfFive(n):
    return int(n**(1/5))**5==n

max_range =250
    

def powers():
    for a in range(1,max_range+1):
        for b in range(a,max_range+1):
            for c in range(b,max_range+1):
                for d in range(c,max_range+1):
                    # print(a,b,c,d)
                    if isPowerOfFive(a**5 + b**5 +c**5+d**5):
                        return (a, b,c,d)
                    continue

print(powers())
