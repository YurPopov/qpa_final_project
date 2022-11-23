from data.operations_db import aa_correspond_to_codon, dna_to_rna

def convert_dna_to_rna(dna_sequence: str):
    '''
    This function uses function from operations_db.py which accesses the database 
    to get RNA bases corresponding to DNA bases.
    '''
    rna_sequence = ''
    for base in dna_sequence:
        new_base = dna_to_rna(base)
        rna_sequence += new_base
    return rna_sequence

def convert_rna_to_protein(rna_sequence: str):
    '''
    This function uses function from operations_db.py which accesses the database 
    to get aminoacids corresponding to codons.
    '''
    
    # create codon chain from RNA sequence
    codon_chain = []
    codon = ''
    for base in rna_sequence:
        codon += base
        if len(codon) == 3:
            codon_chain.append(codon)
            codon = ''

    # create protein using external function, stop codons are absent in DB and we declare they inside function
    stop_codons = ('UAA', 'UAG', 'UGA')
    protein_sequence = ''
    for codon in codon_chain:
        if codon not in stop_codons:
            protein_sequence += aa_correspond_to_codon(codon)
        else:
            protein_sequence += '.'

    return protein_sequence
