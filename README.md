# Quantori Python Academy project - Yury Popov

This project consists of some scripts for manipulating with DNA and RNA sequences and database for storing relations between bases, codons and aminoacids. 

## Installation

Use [docker](https://docker.com) to run container with project.

To deploy - from the root folder:

```bash
cd app
docker-compose up -d --build
```

To switch the containers off:

```bash
docker-compose down -v
```

## How to use functions from bio-application?

1. Firstly, App creates and fills database, then you can use functions.

2. Go to terminal and enter to go to bash in containter
```
docker exec -it bio-app bash
```

2. Using functions for transforming DNA to RNA and RNA to protein. 
```
python transform_seq.py convert_dna_to_rna {seq}
```
Using ths function you can transform DNA sequence to RNA sequence.
Instead {seq} you should write DNA (use only capital letters). 

```
python transform_seq.py convert_rna_to_protein {seq}
```
Using ths function you can transform RNA sequence to aminoacids sequence (protein).
Instead {seq} you should write RNA (use only capital letters). 


3. You can create GC-content plot.
Script uses fasta file from 'external_fastq' folder named 'genomic.fna'. 
Enter in terminal 

```
python gc_plot.py {step}
```
Instead {step} you can enter integer value for "resolution" of plot (default - 100 bases).
Plot is saved to "plots" folder.

## Contributing

Pull requests are welcome. 

Please make sure to update tests as appropriate.
For testing, you can run test_transform_seq.py file from docker, using CLI.
Warning! Test script dictionaries with nucleic acids bases and aminoacids and
doesn't use Postgres database and functions, which access to it.

```
cd tests
python test_transform_seq.py
```
