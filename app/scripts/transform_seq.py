import fire
import sys
sys.path.append('../tests')

try:
    from data.operations_db import aa_correspond_to_codon, dna_to_rna
    from data.operations_db import define_dna_bases, define_rna_bases

except ModuleNotFoundError:
    from for_test_db import define_dna_bases, define_rna_bases
    from for_test_db import aa_correspond_to_codon, dna_to_rna

finally:
    class BioFunc():

        def convert_dna_to_rna(self, dna_sequence: str) -> str:
            # func description for module fire
            '''
            This function transform DNA sequences to RNA sequence.
            Enter DNA sequence after space.
            '''
            dna_sequence = dna_sequence.strip()
            rna_sequence = ''
            dna_bases = define_dna_bases()
            check = set(list(dna_sequence))
            if check.issubset(dna_bases):
                for base in dna_sequence:
                    new_base = dna_to_rna(base)
                    rna_sequence += new_base
                return rna_sequence
            else:
                return 'Enter valid DNA sequence'

        def convert_rna_to_protein(self, rna_sequence: str) -> str:
            # func description for module fire
            '''
            This function transform RNA sequences to protein.
            Enter RNA sequence after space.
            '''

            rna_sequence = rna_sequence.strip()
            rna_bases = define_rna_bases()
            check = set(list(rna_sequence))
            if check.issubset(rna_bases):
                codon_chain = []
                codon = ''
                for base in rna_sequence:
                    codon += base
                    if len(codon) == 3:
                        codon_chain.append(codon)
                        codon = ''

                # create protein using external function, stop codons
                # are absent in DB and we declare they inside function
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

    if __name__ == '__main__':
        fire.Fire(BioFunc)
