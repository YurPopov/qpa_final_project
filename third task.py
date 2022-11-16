import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Bio.Seq import Seq
from Bio.SeqIO import parse


def gc_ratio(sequence: str, step=100):
    
    subsequences = [] 
    subseq = ''
    counter = 0

    for base in sequence:
        subseq += base
        counter += 1
        if counter == 100:
            subsequences.append(subseq)
            counter = 0
            subseq = ''

    
    ratio_list = []
    for subsequence in subsequences:
        number_a = subsequence.count('A')
        number_c = subsequence.count('C')
        number_g = subsequence.count('G')
        number_t = subsequence.count('T')
        ratio = (number_g + number_c) / (number_a + number_t + number_g + number_c) * 100
        ratio_list.append(ratio)

    plt.plot(ratio_list)
    plt.title('GC-content distribution')
    plt.xlabel('Genome position, kilobases')
    plt.ylabel('G-C ratio, %')
    plt.savefig('gc-content.png')

    return 'plot saved!'

file = parse(open('genomic.fna'), 'fasta')
for s in file:
    virus_seq = s.seq

virus_gc_ratio = gc_ratio(virus_seq)










