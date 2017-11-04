from strutils import unique_substrings
if __name__ == "__main__":
    with open('../pi-10million.txt') as pi:
        pi_digits = pi.read().strip()
        unique_occurences = unique_substrings(pi_digits, 7)
    for oc in unique_occurences:
        print(oc)
