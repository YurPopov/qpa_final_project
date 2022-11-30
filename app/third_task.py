import matplotlib.pyplot as plt
from Bio.SeqIO import parse
import sys
from pathlib import Path
import os

args = sys.argv

step = 100

try:
    step = args[1]
except:
    IndexError

way_to_seq = os.getcwd() + str(Path('/external_fastq')) + '/genomic.fna'
way_to_plot = os.getcwd() + str(Path('/plots')) + '/gc-content.png'

def gc_ratio(sequence: str, step=100):
    '''
    This function calculate GC-ratio in the sequence. 
    GC-ratio calculates separately for each 100 bases, for this, subsequences of 
    100 bases are created and stored in a separate list.
    Then plot with calculated values is created and saved to project folder.
    '''
    subsequences = [] 
    subseq = ''
    counter = 0
    step = int(step)

    for base in sequence:
        subseq += base
        counter += 1
        if counter == step:
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
    plt.savefig(way_to_plot)
    print('plot saved to plots folder!') 

# this expression collect primary sequence from fastq file (it should be in external_fastq folder)
file = parse(open(way_to_seq), 'fasta')
for s in file:
    virus_seq = s.seq

# this expression uses gc-function for sequence which was recieved from fastq file
gc_ratio(virus_seq, step)
