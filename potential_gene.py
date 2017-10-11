from array_utils import group3
STOP_CODONS = ['TAA', 'TAG', 'TGA']

def get_codons(seq):
    return [''.join(x) for x in group3(seq)]

def is_potential_gene(dna):
    if len(dna)%3 != 0:
        return False
    codons = get_codons(dna)
    return is_potential_lst_codons(codons)

def is_potential_lst_codons(codons):
    if len(codons) < 2:
        return False
    if codons[0] != 'ATG':
        return False
    if codons[-1] not in STOP_CODONS:
        return False
    for i in range(1, len(codons)-1):
        if codons[i] in STOP_CODONS:
            return False
    return True
    

def get_potential_gene_codons_at_start(sequence):
    codons = get_codons(sequence)
    n = len(codons)
    for i in range(1,n):
        if is_potential_lst_codons(codons[:i+1]):
            return codons[:i+1]
    return []

def get_potential_genes(sequence, min_length=None):
    res = []
    for i in range(len(sequence)):
        gene_codons = get_potential_gene_codons_at_start(sequence[i:])
        if gene_codons != []:
            gene = ''.join(gene_codons)
            if min_length is None:
                res += [gene]
            elif len(gene)>= min_length:
                res += [gene]
    return res
if __name__ == "__main__":
    gs=get_potential_genes('ATGAGCCCCCTTACAACAACAATTCTACTATCAAGCTTAGCAACCGGCACCATCATTACAGCCACAAGCTATCACTGACTATTAGCTTGAATTGGCCTTGAACTAAACACATTAGCTATCATTCCAATTATCTCAAAACAACATCACCCCCGAGCGACAGAGGCCGCCACCAAGTACTTCTTAACTCAAGCAGCTGCTTCAGCACTAATCCTATTCTCAAGTACAATCAACGCTTGACACTCAGGAACTTGGGACATTACACAAATAACAAACAATACATCAAACATCTTACTAACAATGGCACTAGCCATAAAATTAGGCCTTGCACCAACACACTACTGACTCCCAGAGGTTATTCAAGGAACATCAATAACAACAGCCCTAATTATTACTACGTGACAAAAACTAGCCCCTATAGCACTCATTATTATTACAAGCAACAACTTATCCTATATAGTCTTAATAACAATGGGGGTATTATCTACCATCGTAGGAGGATGGGGCGGCCTAAACCAAACCCAAACCCGAAAAATCATAGCGTACTCCTCAATCGCACACCTTGGCTGAATATCAATGGTTACCCCACTAATAACAAAACTACTCATTTTAAACCTTGGCATTTACATCCTAATAACAACAGCTATATTCCTCTCACTAATTTTATCAAAATCAAAAACCTTACAAGATACATCCACACTATGGGCACTATCCCCAACACTTATAATTTTAACAATACTAACACTATTATCCCTAGGAGGACTGCCCCCACTAACAGGATTCATACCCAAGTGACTTATTCTACAAGAATTAACAGCACAAAACCTACTAATAGTAGCCACACTTCTAGCCCTATCAGCACTCTTAAGCCTCTTCTTTTACCTCCGACTAACATACACAATGACCCTTACCACACCCCCCAACACCACTATATTCAAACACAAATGACGGTTTAACTATTTAAATAATACAACTCCCCTATCCATCTCCATAGCCCTCTCAACCCTATTATTACCAATTACACCCCTCATCATAATATAGAAACTTAGGATAACATTAAACCAAGGGCCTTCAAAGCCCAAAATAGGAGTGAAAATCCCCTAGTCTCTGATAAGACCTGTGATATTCTAAAACACATCTTCTGAATGCAACCCAGACAC', min_length=15)
    print(gs)
    

