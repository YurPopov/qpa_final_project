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

1. Creating and filling database, you can use functions.

2. Go to terminal and enter to go to bash in containter
```
docker exec -it bio-app bash
```

2. Using functions for transforming DNA to RNA and RNA to protein. 
```
python first_task_with_db.py {seq}
```
Instead {seq} you can write DNA or RNA sequence (use capital letters) or both (separated with space). 
If you enter only one sequence next step is enter type of sequence - dna or rna.

3. You can create GC-content plot.
Script uses fasta file from 'external_fastq' folder named 'genomic.fna'. 
Enter in terminal 

```
python third_task.py {step}
```
Instead {step} you can enter integer value for "resolution" of plot (default - 100 bases).
Plot is saved to "plots" folder.

## Contributing

Pull requests are welcome. 

Please make sure to update tests as appropriate.
