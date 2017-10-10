import argparse

def sum_digits(n):
    res = n % 9
    return res if res > 0 else res + 9

def sum_ISBN(num, mul=3):
    return sum(int(n) if i %2 == 0 else int(n)*mul for i, n in enumerate(str(num)))

def is_valid_ISBN(num):
    if len(str(num)) != 13:
        return False
    return sum_ISBN(num) %10 == 0

def is_valid_ISBN_str(str_isbn):
    return is_valid_ISBN(str_isbn.replace('-',''))



def sum_digits_Luhn(num, mul=2):
    total = 0
    for i, digit in enumerate(str(num)):
        if i%2 == 0:
            total += int(digit)
        else:
            total += sum_digits(int(digit)*mul)
    return total 

#Luhn's algorithm
def checksum_Luhn(num):
    return  sum_digits_Luhn(num) % 10 == 0

def make_checksum_Luhn(num):
    append = 10 - sum_digits_Luhn(num) % 10
    return int(str(num) + str(append))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Checksum as used in banks')
    parser.add_argument('number', type=int, help='checksum for number: 10 digits to create, 11 digits to check')
    args = parser.parse_args()

    number = str(args.number)
    if(len(number) == 10):
        res = make_checksum_Luhn(number)
        print(res)
    else:
        print(checksum_Luhn(number))

        


