from array_utils import group3
STOP_CODONS = ['TAA', 'TAG', 'TGA']
def is_potential_gene(dna):
    if len(dna)%3 != 0:
        return False
    codons = [''.join(x) for x in group3(dna)]
    if codons[0] != 'ATG':
        return False
    if codons[-1] not in STOP_CODONS:
        return False
    for i in range(1, len(codons)-1):
        if codons[i] in STOP_CODONS:
            return False
    return True
    

def get_potential_genes(sequence, min_length):

