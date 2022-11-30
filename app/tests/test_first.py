import sys
sys.path.append("./")
import unittest
from first_task import convert_dna_to_rna, convert_rna_to_protein

class TestFirstTaskDna(unittest.TestCase):

    def test_norm_seq(self):
        seq = 'AAACCCGGGTTT'
        rna_seq = 'AAACCCGGGUUU'
        rna_from_func = convert_dna_to_rna(seq)
        self.assertEqual(rna_seq, rna_from_func) 
    
    def test_null_seq(self):
        seq = ''
        rna_seq = ''
        rna_from_func = convert_dna_to_rna(seq)
        self.assertEqual(rna_seq, rna_from_func) 

    def test_seq_with_spaces_in_start_and_end(self):
        seq = '    AAACCCGGGTTT     '
        rna_seq = 'AAACCCGGGUUU'
        rna_from_func = convert_dna_to_rna(seq)
        self.assertEqual(rna_seq, rna_from_func) 

    def test_seq_with_spaces_inside(self):
        seq = 'AAACCCG    GGTTT'
        rna_from_func = convert_dna_to_rna(seq)
        self.assertEqual('Enter valid DNA sequence', rna_from_func)    

    def test_seq_with_other_symbols(self):
        seq = 'AAACCCGKJJK!@!34ДОьдljdbTTT'
        rna_from_func = convert_dna_to_rna(seq)
        self.assertEqual('Enter valid DNA sequence', rna_from_func)


class TestFirstTaskRna(unittest.TestCase):

    def test_norm_seq(self):
        seq = 'AAACCCGGGUUU'
        prot_seq = 'KPGF'
        prot_from_func = convert_rna_to_protein(seq)
        self.assertEqual(prot_seq, prot_from_func) 

    def test_short_seq(self):
        seq = 'AAACCCGGGUU'
        prot_seq = 'KPG'
        prot_from_func = convert_rna_to_protein(seq)
        self.assertEqual(prot_seq, prot_from_func) 

    def test_null_seq(self):
        seq = ''
        prot_seq = ''
        prot_from_func = convert_rna_to_protein(seq)
        self.assertEqual(prot_seq, prot_from_func) 

    def test_seq_with_spaces_in_start_and_end(self):
        seq = '    AAACCCGGGUUU     '
        prot_seq = 'KPGF'
        prot_from_func = convert_rna_to_protein(seq)
        self.assertEqual(prot_seq, prot_from_func) 

    def test_seq_with_spaces_inside(self):
        seq = 'AAACCCG    GGTTT'
        prot_from_func = convert_rna_to_protein(seq)
        self.assertEqual('Enter valid RNA sequence', prot_from_func)    

    def test_seq_with_other_symbols(self):
        seq = 'AAACCCGKJJK!@!34ДОьдljdbTTT'
        prot_from_func = convert_rna_to_protein(seq)
        self.assertEqual('Enter valid RNA sequence', prot_from_func)


if __name__ == "__main__":
    unittest.main()