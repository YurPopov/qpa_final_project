# script for filling tables in database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import DnaBases, RnaBases, Codons, AminoAcids

# create engine
engine = create_engine('sqlite:///./data/database_qpa_project.db', echo=True)

# create new session
Session = sessionmaker(autoflush=False, bind=engine)


# create values in tables with DNA and RNA bases 
adenine = DnaBases(
    base = "A",
    dna_base_number = 1
)

guanine = DnaBases(
    base = "G",
    dna_base_number = 2
)

cytosine = DnaBases(
    base = "C",
    dna_base_number = 3
)

thymine = DnaBases(
    base = "T",
    dna_base_number = 4
)

uracil = RnaBases(
    base = "U",
    rna_base_number = 4
)

adenine2 = RnaBases(
    base = "A",
    rna_base_number = 1
)

guanine2 = RnaBases(
    base = "G",
    rna_base_number = 2
)

cytosine2 = RnaBases(
    base = "C",
    rna_base_number = 3
)


with Session() as session:
    session.add(adenine)
    session.add(guanine)
    session.add(cytosine)
    session.add(thymine)
    session.add(uracil)
    session.add(adenine2)
    session.add(guanine2)
    session.add(cytosine2)
    session.commit()


# create values for Aminoacids table

alanine_1 = AminoAcids(
    name = 'alanine',
    letter_name = 'A',
    alias_name = 'Ala',
    rna_codon = 'GCU'
)

alanine_2 = AminoAcids(
    name = 'alanine',
    letter_name = 'A',
    alias_name = 'Ala',
    rna_codon = 'GCC'
)

alanine_3 = AminoAcids(
    name = 'alanine',
    letter_name = 'A',
    alias_name = 'Ala',
    rna_codon = 'GCA'
)

alanine_4 = AminoAcids(
    name = 'alanine',
    letter_name = 'A',
    alias_name = 'Ala',
    rna_codon = 'GCG'
)

arginine_1 = AminoAcids(
    name = 'arginine',
    letter_name = 'R',
    alias_name = 'Arg',
    rna_codon = 'CGU'
)

arginine_2 = AminoAcids(
    name = 'arginine',
    letter_name = 'R',
    alias_name = 'Arg',
    rna_codon = 'CGC'
)

arginine_3 = AminoAcids(
    name = 'arginine',
    letter_name = 'R',
    alias_name = 'Arg',
    rna_codon = 'CGA'
)

arginine_4 = AminoAcids(
    name = 'arginine',
    letter_name = 'R',
    alias_name = 'Arg',
    rna_codon = 'CGG'
)

arginine_5 = AminoAcids(
    name = 'arginine',
    letter_name = 'R',
    alias_name = 'Arg',
    rna_codon = 'AGA'
)

arginine_6 = AminoAcids(
    name = 'arginine',
    letter_name = 'R',
    alias_name = 'Arg',
    rna_codon = 'AGG'
)

asparagine_1 = AminoAcids(
    name = 'asparagine',
    letter_name = 'N',
    alias_name = 'Asn',
    rna_codon = 'AAU'
)

asparagine_2 = AminoAcids(
    name = 'asparagine',
    letter_name = 'N',
    alias_name = 'Asn',
    rna_codon = 'AAC'
)

aspartic_acid_1 = AminoAcids(
    name = 'aspartic_acid',
    letter_name = 'D',
    alias_name = 'Asp',
    rna_codon = 'GAU'
)

aspartic_acid_2 = AminoAcids(
    name = 'aspartic_acid',
    letter_name = 'D',
    alias_name = 'Asp',
    rna_codon = 'GAC'
)

cysteine_1 = AminoAcids(
    name = 'cysteine',
    letter_name = 'C',
    alias_name = 'Cys',
    rna_codon = 'UGU'
)

cysteine_2 = AminoAcids(
    name = 'cysteine',
    letter_name = 'C',
    alias_name = 'Cys',
    rna_codon = 'UGC'
)

glutamine_1 = AminoAcids(
    name = 'glutamine',
    letter_name = 'Q',
    alias_name = 'Gln',
    rna_codon = 'CAA'
)

glutamine_2 = AminoAcids(
    name = 'glutamine',
    letter_name = 'Q',
    alias_name = 'Gln',
    rna_codon = 'CAG'
)

glutamic_acid_1 = AminoAcids(
    name = 'glutamic_acid',
    letter_name = 'E',
    alias_name = 'Glu',
    rna_codon = 'GAA'
)

glutamic_acid_2 = AminoAcids(
    name = 'glutamic_acid',
    letter_name = 'E',
    alias_name = 'Glu',
    rna_codon = 'GAG'
)

glycine_1 = AminoAcids(
    name = 'glycine',
    letter_name = 'G',
    alias_name = 'Gly',
    rna_codon = 'GGU'
)

glycine_2 = AminoAcids(
    name = 'glycine',
    letter_name = 'G',
    alias_name = 'Gly',
    rna_codon = 'GGC'
)

glycine_3 = AminoAcids(
    name = 'glycine',
    letter_name = 'G',
    alias_name = 'Gly',
    rna_codon = 'GGA'
)

glycine_4 = AminoAcids(
    name = 'glycine',
    letter_name = 'G',
    alias_name = 'Gly',
    rna_codon = 'GGG'
)

histidine_1 = AminoAcids(
    name = 'histidine',
    letter_name = 'H',
    alias_name = 'His',
    rna_codon = 'CAU'
)

histidine_2 = AminoAcids(
    name = 'histidine',
    letter_name = 'H',
    alias_name = 'His',
    rna_codon = 'CAC'
)

isoleucine_1 = AminoAcids(
    name = 'isoleucine',
    letter_name = 'I',
    alias_name = 'Ile',
    rna_codon = 'AUU'
)

isoleucine_2 = AminoAcids(
    name = 'isoleucine',
    letter_name = 'I',
    alias_name = 'Ile',
    rna_codon = 'AUC'
)

isoleucine_3 = AminoAcids(
    name = 'isoleucine',
    letter_name = 'I',
    alias_name = 'Ile',
    rna_codon = 'AUA'
)

leucine_1 = AminoAcids(
    name = 'leucine',
    letter_name = 'L',
    alias_name = 'Leu',
    rna_codon = 'UUA'
)

leucine_2 = AminoAcids(
    name = 'leucine',
    letter_name = 'L',
    alias_name = 'Leu',
    rna_codon = 'UUG'
)

leucine_3 = AminoAcids(
    name = 'leucine',
    letter_name = 'L',
    alias_name = 'Leu',
    rna_codon = 'CUU'
)

leucine_4 = AminoAcids(
    name = 'leucine',
    letter_name = 'L',
    alias_name = 'Leu',
    rna_codon = 'CUC'
)

leucine_5 = AminoAcids(
    name = 'leucine',
    letter_name = 'L',
    alias_name = 'Leu',
    rna_codon = 'CUA'
)

leucine_6 = AminoAcids(
    name = 'leucine',
    letter_name = 'L',
    alias_name = 'Leu',
    rna_codon = 'CUG'
)

lysine_1 = AminoAcids(
    name = 'lysine',
    letter_name = 'K',
    alias_name = 'Lys',
    rna_codon = 'AAA'
)

lysine_2 = AminoAcids(
    name = 'lysine',
    letter_name = 'K',
    alias_name = 'Lys',
    rna_codon = 'AAG'
)

methionine = AminoAcids(
    name = 'methionine',
    letter_name = 'M',
    alias_name = 'Met',
    rna_codon = 'AUG'
)

phenylalanine_1 = AminoAcids(
    name = 'phenylalanine',
    letter_name = 'F',
    alias_name = 'Phe',
    rna_codon = 'UUU'
)

phenylalanine_2 = AminoAcids(
    name = 'phenylalanine',
    letter_name = 'F',
    alias_name = 'Phe',
    rna_codon = 'UUC'
)


proline_1 = AminoAcids(
    name = 'proline',
    letter_name = 'P',
    alias_name = 'Pro',
    rna_codon = 'CCU'
)

proline_2 = AminoAcids(
    name = 'proline',
    letter_name = 'P',
    alias_name = 'Pro',
    rna_codon = 'CCC'
)

proline_3 = AminoAcids(
    name = 'proline',
    letter_name = 'P',
    alias_name = 'Pro',
    rna_codon = 'CCA'
)

proline_4 = AminoAcids(
    name = 'proline',
    letter_name = 'P',
    alias_name = 'Pro',
    rna_codon = 'CCG'
)

serine_1 = AminoAcids(
    name = 'serine',
    letter_name = 'S',
    alias_name = 'Ser',
    rna_codon = 'UCU'
)

serine_2 = AminoAcids(
    name = 'serine',
    letter_name = 'S',
    alias_name = 'Ser',
    rna_codon = 'UCC'
)

serine_3 = AminoAcids(
    name = 'serine',
    letter_name = 'S',
    alias_name = 'Ser',
    rna_codon = 'UCA'
)

serine_4 = AminoAcids(
    name = 'serine',
    letter_name = 'S',
    alias_name = 'Ser',
    rna_codon = 'UCG'
)

serine_5 = AminoAcids(
    name = 'serine',
    letter_name = 'S',
    alias_name = 'Ser',
    rna_codon = 'AGU'
)

serine_6 = AminoAcids(
    name = 'serine',
    letter_name = 'S',
    alias_name = 'Ser',
    rna_codon = 'AGC'
)

threonine_1 = AminoAcids(
    name = 'threonine',
    letter_name = 'T',
    alias_name = 'Thr',
    rna_codon = 'ACU'
)

threonine_2 = AminoAcids(
    name = 'threonine',
    letter_name = 'T',
    alias_name = 'Thr',
    rna_codon = 'ACC'
)

threonine_3 = AminoAcids(
    name = 'threonine',
    letter_name = 'T',
    alias_name = 'Thr',
    rna_codon = 'ACA'
)

threonine_4 = AminoAcids(
    name = 'threonine',
    letter_name = 'T',
    alias_name = 'Thr',
    rna_codon = 'ACG'
)

tryptophan_1 = AminoAcids(
    name = 'tryptophan',
    letter_name = 'W',
    alias_name = 'Trp',
    rna_codon = 'UGG'
)

thyrosine_1 = AminoAcids(
    name = 'thyrosine',
    letter_name = 'Y',
    alias_name = 'Tyr',
    rna_codon = 'UAU'
)

thyrosine_2 = AminoAcids(
    name = 'thyrosine',
    letter_name = 'Y',
    alias_name = 'Tyr',
    rna_codon = 'UAC'
)

valine_1 = AminoAcids(
    name = 'valine',
    letter_name = 'V',
    alias_name = 'Val',
    rna_codon = 'GUU'
)

valine_2 = AminoAcids(
    name = 'valine',
    letter_name = 'V',
    alias_name = 'Val',
    rna_codon = 'GUC'
)

valine_3 = AminoAcids(
    name = 'valine',
    letter_name = 'V',
    alias_name = 'Val',
    rna_codon = 'GUA'
)

valine_4 = AminoAcids(
    name = 'valine',
    letter_name = 'V',
    alias_name = 'Val',
    rna_codon = 'GUG'
)


with Session() as session:
    session.add(alanine_1)
    session.add(alanine_2)
    session.add(alanine_3)
    session.add(alanine_4)
    session.add(arginine_1)
    session.add(arginine_2)
    session.add(arginine_3)
    session.add(arginine_4)
    session.add(arginine_5)
    session.add(arginine_6)
    session.add(asparagine_1)
    session.add(asparagine_2)
    session.add(aspartic_acid_1)
    session.add(aspartic_acid_2)
    session.add(cysteine_1)
    session.add(cysteine_2)
    session.add(glutamine_1)
    session.add(glutamine_2)
    session.add(glutamic_acid_1)
    session.add(glutamic_acid_2)
    session.add(glycine_1)
    session.add(glycine_2)
    session.add(glycine_3)
    session.add(glycine_4)
    session.add(histidine_1)
    session.add(histidine_2)
    session.add(isoleucine_1)
    session.add(isoleucine_2)
    session.add(isoleucine_3)
    session.add(leucine_1)
    session.add(leucine_2)
    session.add(leucine_3)
    session.add(leucine_4)
    session.add(leucine_5)
    session.add(leucine_6)
    session.add(lysine_2)
    session.add(lysine_1)
    session.add(methionine)
    session.add(phenylalanine_1)
    session.add(phenylalanine_2)
    session.add(proline_1)
    session.add(proline_2)
    session.add(proline_3)
    session.add(proline_4)
    session.add(serine_1)
    session.add(serine_2)
    session.add(serine_3)
    session.add(serine_4)
    session.add(serine_5)
    session.add(serine_6)
    session.add(threonine_1)
    session.add(threonine_2)
    session.add(threonine_3)
    session.add(threonine_4)
    session.add(tryptophan_1)
    session.add(thyrosine_1)
    session.add(thyrosine_2)
    session.add(valine_1)
    session.add(valine_2)
    session.add(valine_3)
    session.add(valine_4)
    session.commit()

# create values for codons table

codon_1 = Codons(
    name = 'UUU',
    aminoacid = 'F'
)

codon_2 = Codons(
    name = 'UUC',
    aminoacid = 'F'
)

codon_3 = Codons(
    name = 'UUA',
    aminoacid = 'L'
)

codon_4 = Codons(
    name = 'UUG',
    aminoacid = 'L'
)

codon_5 = Codons(
    name = 'CUU',
    aminoacid = 'L'
)

codon_6 = Codons(
    name = 'CUC',
    aminoacid = 'L'
)

codon_7 = Codons(
    name = 'CUA',
    aminoacid = 'L'
)

codon_8 = Codons(
    name = 'CUG',
    aminoacid = 'L'
)

codon_9 = Codons(
    name = 'AUU',
    aminoacid = 'I'
)

codon_10 = Codons(
    name = 'AUC',
    aminoacid = 'I'
)

codon_11 = Codons(
    name = 'AUA',
    aminoacid = 'I'
)

codon_12 = Codons(
    name = 'AUG',
    aminoacid = 'M'
)

codon_13 = Codons(
    name = 'GUU',
    aminoacid = 'V'
)

codon_14 = Codons(
    name = 'GUC',
    aminoacid = 'V'
)

codon_15 = Codons(
    name = 'GUA',
    aminoacid = 'V'
)

codon_16 = Codons(
    name = 'GUG',
    aminoacid = 'V'
)

codon_17 = Codons(
    name = 'UCU',
    aminoacid = 'S'
)

codon_18 = Codons(
    name = 'UCC',
    aminoacid = 'S'
)

codon_19 = Codons(
    name = 'UCA',
    aminoacid = 'S'
)

codon_20 = Codons(
    name = 'UCG',
    aminoacid = 'S'
)

codon_21 = Codons(
    name = 'CCU',
    aminoacid = 'P'
)

codon_22 = Codons(
    name = 'CCC',
    aminoacid = 'P'
)

codon_23 = Codons(
    name = 'CCA',
    aminoacid = 'P'
)

codon_24 = Codons(
    name = 'CCG',
    aminoacid = 'P'
)

codon_25 = Codons(
    name = 'ACU',
    aminoacid = 'T'
)

codon_26 = Codons(
    name = 'ACC',
    aminoacid = 'T'
)

codon_27 = Codons(
    name = 'ACA',
    aminoacid = 'T'
)

codon_28 = Codons(
    name = 'ACG',
    aminoacid = 'T'
)

codon_29 = Codons(
    name = 'UAU',
    aminoacid = 'Y'
)

codon_30 = Codons(
    name = 'UAC',
    aminoacid = 'Y'
)

codon_31 = Codons(
    name = 'CAU',
    aminoacid = 'H'
)

codon_32 = Codons(
    name = 'CAC',
    aminoacid = 'H'
)

codon_33 = Codons(
    name = 'CAA',
    aminoacid = 'Q'
)

codon_34 = Codons(
    name = 'CAG',
    aminoacid = 'Q'
)

codon_35 = Codons(
    name = 'AAU',
    aminoacid = 'N'
)

codon_36 = Codons(
    name = 'AAC',
    aminoacid = 'N'
)

codon_37 = Codons(
    name = 'AAA',
    aminoacid = 'K'
)

codon_38 = Codons(
    name = 'AAG',
    aminoacid = 'K'
)

codon_39 = Codons(
    name = 'GAU',
    aminoacid = 'D'
)

codon_40 = Codons(
    name = 'GAC',
    aminoacid = 'D'
)

codon_41 = Codons(
    name = 'GAA',
    aminoacid = 'E'
)

codon_42 = Codons(
    name = 'GAG',
    aminoacid = 'E'
)

codon_43 = Codons(
    name = 'UGU',
    aminoacid = 'C'
)

codon_44 = Codons(
    name = 'UGC',
    aminoacid = 'C'
)

codon_45 = Codons(
    name = 'UGG',
    aminoacid = 'W'
)

codon_46 = Codons(
    name = 'CGU',
    aminoacid = 'R'
)

codon_47 = Codons(
    name = 'CGC',
    aminoacid = 'R'
)

codon_48 = Codons(
    name = 'CGA',
    aminoacid = 'R'
)

codon_49 = Codons(
    name = 'CGG',
    aminoacid = 'R'
)

codon_50 = Codons(
    name = 'AGU',
    aminoacid = 'S'
)

codon_51 = Codons(
    name = 'AGC',
    aminoacid = 'S'
)

codon_52 = Codons(
    name = 'AGA',
    aminoacid = 'R'
)

codon_53 = Codons(
    name = 'AGG',
    aminoacid = 'R'
)

codon_54 = Codons(
    name = 'GGU',
    aminoacid = 'G'
)

codon_55 = Codons(
    name = 'GGC',
    aminoacid = 'G'
)

codon_56 = Codons(
    name = 'GGA',
    aminoacid = 'G'
)

codon_57 = Codons(
    name = 'GGG',
    aminoacid = 'G'
)

with Session() as session:
    session.add(codon_1)
    session.add(codon_2)
    session.add(codon_3)
    session.add(codon_4)
    session.add(codon_5)
    session.add(codon_6)
    session.add(codon_7)
    session.add(codon_8)
    session.add(codon_9)
    session.add(codon_10)
    session.add(codon_11)
    session.add(codon_12)
    session.add(codon_13)
    session.add(codon_14)
    session.add(codon_15)
    session.add(codon_16)
    session.add(codon_17)
    session.add(codon_18)
    session.add(codon_19)
    session.add(codon_20)
    session.add(codon_21)
    session.add(codon_22)
    session.add(codon_23)
    session.add(codon_24)
    session.add(codon_25)
    session.add(codon_26)
    session.add(codon_27)
    session.add(codon_28)
    session.add(codon_29)
    session.add(codon_30)
    session.add(codon_31)
    session.add(codon_32)
    session.add(codon_33)
    session.add(codon_34)
    session.add(codon_35)
    session.add(codon_36)
    session.add(codon_37)
    session.add(codon_38)
    session.add(codon_39)
    session.add(codon_40)
    session.add(codon_41)
    session.add(codon_42)
    session.add(codon_43)
    session.add(codon_44)
    session.add(codon_45)
    session.add(codon_46)
    session.add(codon_47)
    session.add(codon_48)
    session.add(codon_49)
    session.add(codon_50)
    session.add(codon_51)
    session.add(codon_52)
    session.add(codon_53)
    session.add(codon_54)
    session.add(codon_55)
    session.add(codon_56)
    session.add(codon_57)
    session.commit()