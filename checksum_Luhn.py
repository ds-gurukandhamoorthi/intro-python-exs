import argparse

def sum_digits(n):
    res = n % 9
    return res if res > 0 else res + 9

def sum_digits_Luhn(num):
    total = 0
    for i, digit in enumerate(str(num)):
        if i%2 == 0:
            total += int(digit)
        else:
            total += sum_digits(int(digit)*2)
    return total 

#Luhn's algorithm
def checksum_Luhn(num):
    return  sum_digits_Luhn(num) % 10 == 0

def make_checksum_Luhn(num):
    append = 10 - sum_digits_Luhn(num) % 10
    return int(str(num) + str(append))




parser = argparse.ArgumentParser(description='Checksum as used in banks')
parser.add_argument('number', type=int, help='checksum for number: 10 digits to create, 11 digits to check')
args = parser.parse_args()

number = str(args.number)
if(len(number) == 10):
    res = make_checksum_Luhn(number)
    print(res)
else:
    print(checksum_Luhn(number))

    


