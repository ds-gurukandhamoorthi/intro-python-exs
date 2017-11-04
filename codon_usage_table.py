from collections import Counter
from Genome import Genome

if __name__ == "__main__":
    with open('../genome') as genome:
        sequence = genome.read().strip()
        genome = Genome(sequence)
        codon_count = Counter()
        for codon in genome:
            codon_count[codon] += 1
    total = sum(codon_count.values())
    for codon, count in codon_count.items():
        print(codon, count/total)

