'''
With this file we create database which contains tables with DNA abd RNA bases, 
aminoacins and codons, define relations.
'''

from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# create adress for database
SQLALCHEMY_DATABASE_URL = 'sqlite:///./data/database_qpa_project.db'

# create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base()

# create base for DNA
class DnaBases(Base):
     __tablename__ = 'dna_bases'

     base = Column(String(1), comment='DNA base')
     dna_base_number = Column(Integer, primary_key=True, comment='Key for connecting with rna_bases Table')
     dna_rna_rel = relationship('RnaBases', backref='dna_base_number', uselist=False)


     def __repr__(self):
         return f'{self.base}'

# create base for RNA
class RnaBases(Base):
     __tablename__ = 'rna_bases'

     base_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
     base = Column(String(1), comment='RNA base')
     rna_base_number = Column(Integer, ForeignKey('dna_bases.dna_base_number'))

     def __repr__(self):
         return f'{self.base}'

# create base for aminoacids
class AminoAcids(Base):
     __tablename__ = 'amino_acids'
     
     name = Column(String(20), comment='aminoacid name')
     letter_name = Column(String(1), comment='abbreviation for aminoacid')
     alias_name = Column(String(3), comment='3-letter name of aminoacid')
     rna_codon = Column(String(3), primary_key=True, comment='RNA codon corresponded to aminoacid')

     def __repr__(self):
         return f'{self.letter_name}'

# create base for codons
class Codons(Base):
     __tablename__ = 'codons'
     
     codon_id = Column(Integer, nullable=False, unique=True, autoincrement=True, primary_key=True)
     name = Column(String(3), ForeignKey('amino_acids.rna_codon'))
     aminoacid = Column(String(1))
     aa = relationship('AminoAcids')
     
     def __repr__(self):
         return f'{self.codon_id} {self.name}'

#create file with DB in project folder
Base.metadata.create_all(engine)