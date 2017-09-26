import argparse
import matplotlib.pyplot as plt

def convert_base(n, base_array):
    res = [0] * len(base_array)
    for i,val in enumerate(base_array):
        if val != 0:
            res[i] = n // val
            n %= val
    return res


def encoding(n):
    n = int(n)
    if n == 0:
        return [1,1,0,0,0]
    BASE_ARRAY= [7,4,2,1,0]
    res = convert_base(n, BASE_ARRAY)
    if sum(res) < 2:
        res[-1] = 1 #make the last digit 1 to have exactly two spikes on the postnet code
    return res

def postnet(n):
    if n <= 9999: #postnet 5-digits including checksum
        digits = convert_base(n, [1000,100,10,1])
    else: #postnet 9-digits including checksum
        digits = convert_base(n, [10**i  for i in reversed(range(8))])
    check_sum = sum(digits)%10
    to_enc = digits + [check_sum]
    res = [1] #guard rail
    for val in to_enc:
        res += encoding(val)
    return res + [1] #guard rail



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create postnet for 4 or 8 digit numbers')
    parser.add_argument('number', type=int, help='number for which postnet code must be generated')
    args = parser.parse_args()

    # for i in range(10):
    #     print(i,encoding(str(i)))
    number = args.number
    to_plot = [n + 1 for n in postnet(number)]
    plt.bar(range(len(to_plot)),to_plot)
    plt.axis('off')
    plt.show()




