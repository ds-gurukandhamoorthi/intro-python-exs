from collections import Counter
def count_flames(his_name, her_name):
    "Calculates number of letters remaining after striking out common letter on a one-on-one basis"
    c1 = Counter(his_name)
    c2 = Counter(her_name)
    diff = (c1 | c2) - (c1 & c2)
    return sum(diff.values())

def strike(string, n):
    print(string,n)
    if len(string) <= 1:
        return string
    d =  (n-1) % len(string)   #delete index; one is added as it's one-based counting
    new_string = string[d+1:]+string[:d]
    return strike(new_string, n)
    
if __name__ == "__main__":
    strike('flames',15)
    strike('flame',15)
    strike('flames',12)
    strike('flame',12)
