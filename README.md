# Quantori Python Academy project - Yury Popov

This project consists of some scripts for manipulating with DNA and RNA sequences and database for storing relations between bases, codons and aminoacids. 

## Installation

Use [docker](https://docker.com) to run container with project.

```bash
docker run my_pretty_dnas
```

## Composing

The project has next structure

project folder
|_ data_
|       |_ database_qpa_project.db          # database (DB) with dna_base, rna_base, codon and aminoacids
|       |_ fill_db.py                       # script for DB filling
|       |_ model.py                         # script for creating DB file, declaring fields and relations
|       |_ operations_db.py                 # script for requesting to DB
|
|_ external_fastq___                        # folter for external fastq files
|                   |_ genomic.fna          # fastq file with DNA sequence
|
|_ plots____                                # folder for saving plots
|           |_ gc_content.png
|
|_ tests                                    # folder for storing tests
|
|_ first_task_with_db.py                    # script for transformation DNA to RNA and RNA to protein using DB
|_ first_task.py                            # script for transformation DNA to RNA and RNA to protein
|_ readme.md
|_ requirements.txt                         # names and versions of libraries
|_ third_task.py                            # script for GC-index calculation and plot creation



## Contributing

Pull requests are welcome. 

Please make sure to update tests as appropriate.

