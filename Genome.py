from potential_gene import is_potential_gene
class Genome:
    def __init__(self, sequence):
        if len(sequence) % 3 != 0:
            raise Exception('DNA sequence must have a length that is multiple of 3')
        self._sequence = sequence

    def __iadd__(self, codons):
        if len(codons) % 3 != 0:
            raise Exception('codon length must have a length that is multiple of 3')
        self._sequence += codons
        return self

    def __str__(self):
        return self._sequence

    def __getitem__(self, index):
        if isinstance(index, int):
            return self._sequence[index: index+3]

    def base_at(self, index):
        return self._sequence[index]

    def is_potential_gene(self):
        return is_potential_gene(self._sequence)

if __name__ == "__main__":
    a = 'ATGCGCCTGCGTCTGTACTAG'
    g = Genome(a)
    print(g, g.base_at(3), g.is_potential_gene(), g[0])

        
