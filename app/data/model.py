# With this file we create database which contains tables with DNA
# and RNA bases, aminoacins and codons, define relations.
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URL
sys.path.append('./app/data')

# create engine
Base = declarative_base()


# create base for DNA
class DnaBases(Base):
    __tablename__ = 'dna_bases'

    base = Column(String(1), comment='DNA base')
    dna_base_number = Column(
        Integer, primary_key=True, comment='Key for connecting with rna_bases'
        )
    dna_rna_rel = relationship(
        'RnaBases', backref='dna_base_number', uselist=False)

    def __repr__(self):
        return f'{self.base}'


# create base for RNA
class RnaBases(Base):
    __tablename__ = 'rna_bases'

    base_id = Column(
        Integer, nullable=False, autoincrement=True, primary_key=True
        )
    base = Column(String(1), comment='RNA base')
    rna_base_number = Column(Integer, ForeignKey('dna_bases.dna_base_number'))

    def __repr__(self):
        return f'{self.base}'


# create base for aminoacids
class AminoAcids(Base):
    __tablename__ = 'amino_acids'

    letter_name = Column(String(1), comment='abbreviation for aminoacid')
    name = Column(String(15), comment='AA full name')
    abbr = Column(String(3), comment='3-letter AA name')
    rna_codon = Column(
        String(3), primary_key=True, comment='RNA codon corresponded to AA'
        )

    def __repr__(self):
        return f'{self.letter_name}'


# create base for codons
class Codons(Base):
    __tablename__ = 'codons'

    codon_id = Column(
        Integer, nullable=False, unique=True,
        autoincrement=True, primary_key=True
        )
    name = Column(String(3), ForeignKey('amino_acids.rna_codon'))
    aminoacid = Column(String(1))
    aa = relationship('AminoAcids')

    def __repr__(self):
        return f'{self.codon_id} {self.name}'


def create_base(base):
    engine = create_engine(DATABASE_URL)
    base.metadata.create_all(engine)
    return engine
