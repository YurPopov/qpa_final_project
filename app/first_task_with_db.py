from data2.operations_db import aa_correspond_to_codon, dna_to_rna
import sys

dna = None
rna = None

args = sys.argv

if len(args) == 3:
    dna = args[1]
    rna = args[2]
elif len(args) == 2:
    print('Is it DNA sequence or RNA')
    a = input('dna or rna')
    if a.lower().strip() == 'dna':
        dna = args[1]
    elif a.lower().strip() == 'rna':
        rna = args[1]
    else:
        print('Enter valid value')


def convert_dna_to_rna(dna_sequence: str):
    '''
    This function uses function from operations_db.py which accesses the database 
    to get RNA bases corresponding to DNA bases.
    '''
    dna_sequence = dna_sequence.strip()
    rna_sequence = ''
    dna_bases = {'A', 'C', 'G', 'T'}
    check = set(list(dna_sequence))
    if check.issubset(dna_bases):
        for base in dna_sequence:
            new_base = dna_to_rna(base)
            rna_sequence += new_base
        return rna_sequence
    else:
        return 'Enter valid DNA sequence'

if dna is not None:
    print('DNA to RNA -', convert_dna_to_rna(dna))

def convert_rna_to_protein(rna_sequence: str):
    '''
    This function uses function from operations_db.py which accesses the database 
    to get aminoacids corresponding to codons.
    '''
    
    rna_sequence = rna_sequence.strip()
    rna_bases = {'A', 'C', 'G', 'U'}
    check = set(list(rna_sequence))
    if check.issubset(rna_bases):
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
    else:
        return 'Enter valid RNA sequence'

if rna is not None:
    print('RNA to protein -', convert_rna_to_protein(rna))
