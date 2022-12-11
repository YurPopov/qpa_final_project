# script for filling tables in database
import sys
from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import DnaBases, RnaBases, Codons, AminoAcids, Base, create_base
from config import DATABASE_URL
sys.path.append('./app/data')


dna_bases = ['A', 'G', 'C', 'T']
rna_bases = ['A', 'G', 'C', 'U']
aminoacids = {
    ('A', 'Ala', 'Alanine'): ('GCU', 'GCC', 'GCA', 'GCG'),
    ('R', 'Arg', 'Arginine'): ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
    ('N', 'Asn', 'Asparagine'): ('AAU', 'AAC'),
    ('D', 'Asp', 'Aspartic acid'): ('GAU', 'GAC'),
    ('C', 'Cys', 'Cysteine'): ('UGU', 'UGC'),
    ('Q', 'Gln', 'Glutamine'): ('CAA', 'CAG'),
    ('E', 'Glu', 'Glatamic acid'): ('GAA', 'GAG'),
    ('G', 'Gly', 'Glycine'): ('GGU', 'GGC', 'GGA', 'GGG'),
    ('H', 'His', 'Histidine'): ('CAU', 'CAC'),
    ('I', 'Ile', 'Isoleucine'): ('AUU', 'AUC', 'AUA'),
    ('L', 'Leu', 'Leucine'): ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'),
    ('K', 'Lys', 'Lysine'): ('AAA', 'AAG'),
    ('M', 'Met', 'Methionine'): ('AUG',),
    ('F', 'Phe', 'Phenylalanine'): ('UUU', 'UUC'),
    ('P', 'Pro', 'Proline'): ('CCU', 'CCC', 'CCA', 'CCG'),
    ('S', 'Ser', 'Serine'): ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'),
    ('T', 'Thr', 'Threonine'): ('ACU', 'ACC', 'ACA', 'ACG'),
    ('W', 'Trp', 'Tryptophan'): ('UGG', ),
    ('Y', 'Tyr', 'Tyrosine'): ('UAU', 'UAC'),
    ('V', 'Val', 'Valine'): ('GUU', 'GUC', 'GUA', 'GUG'),
    ('.', '.', 'STOP'): ('UAA', 'UAG', 'UGA')
    }


def fill():
    engine = create_engine(DATABASE_URL)

    # create new session
    Session = sessionmaker(autoflush=False, bind=engine)

    # create values in tables with DNA and RNA bases from lists
    with Session() as session:
        for num in range(len(dna_bases)):
            session.add(DnaBases(base=dna_bases[num], dna_base_number=num+1))

        for num in range(len(rna_bases)):
            session.add(RnaBases(base=rna_bases[num], rna_base_number=num+1))

        session.commit()

    # create values for Aminoacids and Codons tables from dict
    with Session() as session:
        for key, value in aminoacids.items():
            for codon in value:
                session.add(AminoAcids(
                    letter_name=key[0], name=key[2], abbr=key[1], rna_codon=codon)
                    )
                session.add(Codons(name=codon, aminoacid=key[0]))
        session.commit()


if __name__ == '__main__':
    sleep(3)
    create_base(base=Base)
    fill()
    print("Yay, me done!")
