from enum import IntEnum
from typing import Tuple, List


Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # Type alias of codon
Gene = List[Codon]  # Type alias of DNA

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):  # End of data
            return gene
        codon: Codon = (
            Nucleotide[s[i]],
            Nucleotide[s[i + 1]],
            Nucleotide[s[i + 2]]
            )
        gene.append(codon)
    return gene

my_gene: Gene = string_to_gene(gene_str)


def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    """
    Linear search
    """
    for codon in gene:
        if codon == key_codon:
            return True
    return False


acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(linear_contains(my_gene, acg))  # True
print(linear_contains(my_gene, gat))  # False


def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    """
    Binary search
    """
    # Define search region
    low: int = 0
    high: int = len(gene) - 1
    # Continue searching while there is search region
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:  # If the searching element is at the latter half part,
            low = mid + 1  # Update low by the next element of current mid
        elif gene[mid] > key_codon:  # If it is at the former half part,
            high = mid - 1  # Update high by the previous element of current mid
        else:  # If it is not bigger nor smaller than the middle element,
            return True  # It is found!
    return False


my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))
