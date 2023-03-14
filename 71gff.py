# 71gff.py

# Write a program that converts genes in gff into JSON
# Use the minaturized version of the C. elegans genome (included) this time
# Organize the genes onto chromosomes
# Print the number of genes on each chromosome to stderr
# Your code should mimic the output below

# Hint: your outer data structure is a dictionary

# Note: gene names are stored differently here than the last file

import argparse
import json
import re
import gzip

parser = argparse.ArgumentParser(description='Genes in GFF --> JSON')
parser.add_argument('file', type=str, metavar='<path>', help='GFF File')
arg = parser.parse_args()


chromosomes = {}
genome = {}

with gzip.open(arg.file, 'rt') as fp:
	for line in fp:
		for match in re.finditer('\s(gene)\s',line):
			
			#Chromosome Counter
			f = line.split()
			chro = f[0]
			if chro not in chromosomes: 
				chromosomes[chro] =0
			chromosomes[chro] += 1
		
			#Coordinate Search
			coor = re.search('\s(\d+)\s(\d+)\s',line)
			beg = int(coor.group(1))
			end = int(coor.group(2))
			
			#Name Search
			name = re.search('sequence_name=(\w+\.\w+)',line)
			gene = str(name.group(1))
			
			#Strand Search
			nyeh = re.search('\.\s(.)\s\.',line)
			strand = nyeh.group(1)
			
			#Gene Details
			all = {}
			
			all["gene"] = gene
			all["beg"] = beg
			all["end"] = end
			all["strand"] = strand
			
			#Adding to Genome Database
			if chro not in genome:
				genome[chro] = []
			
			genome[chro].append(all)


for item in chromosomes:
	print(item, chromosomes[item])

print(json.dumps(genome, indent=4))

"""
python3 71gff.py elegans
I 37
II 57
III 37
IV 41
MtDNA 2
V 41
X 45
{
    "I": [
        {
            "gene": "Y74C9A.6",
            "beg": 3747,
            "end": 3909,
            "strand": "-"
        },
        {
            "gene": "Y74C9A.3",
            "beg": 4116,
            "end": 10230,
            "strand": "-"
        },
...
"""
