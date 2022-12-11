def define_dna_bases():
    return {'A', 'G', 'C', 'T'}


def define_rna_bases():
    return {'A', 'G', 'C', 'U'}


def dna_to_rna(base):
    if base == 'T':
        return 'U'
    else:
        return base


def aa_correspond_to_codon(codon):
    aminoacids = {
        'A': ('GCU', 'GCC', 'GCA', 'GCG'),
        'R': ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
        'N': ('AAU', 'AAC'),
        'D': ('GAU', 'GAC'),
        'C': ('UGU', 'UGC'),
        'Q': ('CAA', 'CAG'),
        'E': ('GAA', 'GAG'),
        'G': ('GGU', 'GGC', 'GGA', 'GGG'),
        'H': ('CAU', 'CAC'),
        'I': ('AUU', 'AUC', 'AUA'),
        'L': ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'),
        'K': ('AAA', 'AAG'),
        'M': 'AUG',
        'F': ('UUU', 'UUC'),
        'P': ('CCU', 'CCC', 'CCA', 'CCG'),
        'S': ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'),
        'T': ('ACU', 'ACC', 'ACA', 'ACG'),
        'W': 'UGG',
        'Y': ('UAU', 'UAC'),
        'V': ('GUU', 'GUC', 'GUA', 'GUG'),
        '.': ('UAA', 'UAG', 'UGA')
    }
    for key, value in aminoacids.items():
        if codon in value:
            return key
