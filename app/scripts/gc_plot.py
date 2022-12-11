import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
from Bio.SeqIO import parse

args = sys.argv

try:
    step = args[1]
except IndexError:
    step = 100

way_to_seq = os.getcwd() + str(Path('/external_fastq')) + '/genomic.fna'
way_to_plot = os.getcwd(

) + str(Path('/plots')) + '/gc-content_res_' + f'{step}' + '_bases.png'


def gc_ratio(sequence: str, step=100):
    '''
    This function calculate GC-ratio in the sequence.
    GC-ratio calculates separately for each 100 bases, for this,
    subsequences of 100 bases are created and stored in a separate list.
    Then plot with calculated values is created and saved to 'plots' folder.
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
        num_a = subsequence.count('A')
        num_c = subsequence.count('C')
        num_g = subsequence.count('G')
        num_t = subsequence.count('T')
        ratio = (num_g + num_c) / (num_a + num_t + num_g + num_c) * 100
        ratio_list.append(ratio)

    plt.plot(ratio_list)
    plt.title('GC-content distribution')
    plt.xlabel('Genome position, kilobases')
    plt.ylabel('G-C ratio, %')
    plt.savefig(way_to_plot)
    print('plot saved to plots folder!')


# this expression collect primary sequence from fastq file
# (it should be in external_fastq folder)
file = parse(open(way_to_seq), 'fasta')
for s in file:
    virus_seq = s.seq

# this expression uses gc-func for sequence which was recieved from fastq file
gc_ratio(virus_seq, step)
