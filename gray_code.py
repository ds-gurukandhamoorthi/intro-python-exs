def prepend(char, list_str):
    return [char + s for s in list_str]

def gray_code_str(nb_bits):
    if nb_bits == 1:
        return ['0','1']
    prev = gray_code_str(nb_bits-1)
    return prepend('0', prev) + prepend('1',reversed(prev))

def gray_code(nb_bits):
    return [int('0b'+s,2) for s in gray_code_str(nb_bits)]

if __name__ == "__main__":
    print(gray_code_str(1))
    print(gray_code(1))
    print(gray_code_str(3))
    print(gray_code(3))
    print(gray_code_str(4))
    print(gray_code(4))
