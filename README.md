# Quantori Python Academy project - Yury Popov

This project consists of some scripts for manipulating with DNA and RNA sequences and database for storing relations between bases, codons and aminoacids. 

## Installation

Use [docker](https://docker.com) to run container with project.

To deploy - from the root folder:

```bash
docker-compose up -d --build
```

To switch the containers off:

```bash
docker-compose down -v
```

## How to use functions from bio-application?

1. After introduction "Enter DNA sequence to convert it to RNA" you can enter a sequence of DNA for transforming it into RNA.

2. Next step is "Enter RNA sequence to convert it to protein" - enter RNA sequence to transform it into protein.

3. The last one function is GC plot. After message "Let's create GC-content plot of SARS-CoV2 genome. It will be saved to Plots folder", you can enter integer value for 'resolution' of plot (default is 100 bases).


## Contributing

Pull requests are welcome. 

Please make sure to update tests as appropriate.
