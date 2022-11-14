def convert_dna_to_rna(dna_sequence: str):
    rna_sequence = dna_sequence.replace('T', 'U')
    return rna_sequence

def convert_rna_to_protein(rna_sequence: str):
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

    codon_chain = []
    codon = ''
    for base in rna_sequence:
        codon += base
        if len(codon) == 3:
            codon_chain.append(codon)
            codon = ''

    protein_sequence = []
    for codon in codon_chain:
        for k, v in aminoacids.items():
            if codon in v:
                protein_sequence.append(k)

    end_protein_sequence = ''.join(protein_sequence)
    return end_protein_sequence

