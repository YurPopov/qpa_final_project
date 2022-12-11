# this script gets data for functions working with
# dna-to-rna transformation and translation
import sys
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import RnaBases, DnaBases, Codons, AminoAcids
from config import DATABASE_URL
sys.path.append('./app/data')

# create engine and session foe this script
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


# use context manager for automatically closing database after each request.
@contextmanager
def get_session():
    db = SessionLocal()
    yield db
    db.close()


def define_dna_bases():
    '''
    This function takes all available DNA bases from DB
    '''
    with get_session() as db:
        request_to_db = db.query(DnaBases).all()
        dna_bases = set()
        for base in request_to_db:
            base = str(base)
            dna_bases.add(base)
        return dna_bases


def define_rna_bases():
    '''
    This function takes all available DNA bases from DB
    '''
    with get_session() as db:
        request_to_db = db.query(RnaBases).all()
        rna_bases = set()
        for base in request_to_db:
            base = str(base)
            rna_bases.add(base)
        return rna_bases


def aa_correspond_to_codon(ext_codon):
    '''
    This function takes codon and returns corresponding aminoacid.
    Relation between codons and amino_acids tables in database is used.
    In function body, firstly we get request to database as class, then
    convert it into string and take second symbol
    corresponding to needed aminoacid.
    '''
    with get_session() as db:
        request_to_db = db.query(
            AminoAcids).join(Codons).filter(Codons.name == ext_codon).all()
        aminoacid = str(request_to_db)
        return aminoacid[1]


def dna_to_rna(ext_base):
    '''
    This function takes DNA base and returns corresponding RNA base.
    Relation between dna_base and rna_base tables in database is used.
    In function body, firstly we get request to database as class, then
    convert it into string and take second symbol corresponding to needed base.
    '''
    with get_session() as db:
        request_to_db = db.query(
            RnaBases).join(DnaBases).filter(DnaBases.base == ext_base).all()
        base = str(request_to_db)
        return base[1]
