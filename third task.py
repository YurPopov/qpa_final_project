import matplotlib.pyplot as plt
from Bio.SeqIO import parse


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
    plt.savefig('./plots/gc-content.png')

    print('plot saved to plots folder!') 

# this expression collect primary sequence from fastq file (it should be in external_fastq folder)
file = parse(open('./external_fastq/genomic.fna'), 'fasta')
for s in file:
    virus_seq = s.seq

# this expression uses gc-function for sequence which was recieved from fastq file
virus_gc_ratio = gc_ratio(virus_seq)










