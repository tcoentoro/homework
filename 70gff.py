# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

import json
import argparse
import gzip
import re

parser = argparse.ArgumentParser(description='Genes in GFF --> Json')
parser.add_argument('file', type=str, metavar='<path>', help='GFF file' )
arg = parser.parse_args()

genomelist =[]

with gzip.open(arg.file, 'rt') as fp:
	for line in fp:
		if line.startswith('#'): continue
		for match in re.finditer('RefSeq\sgene', line):
			all = {}
			
			#Coordinate Search
			coor = re.search('(\d+)\s(\d+)', line)
			beg = int(coor.group(1))
			end = int(coor.group(2))
			
			#Strand Search
			nyeh = re.search('\.\s(.)\s\.', line)
			strand = nyeh.group(1)
			
			#Name Search
			name = re.search('Name=(\w+)', line)
			gene = str(name.group(1))
			
			#Dictionary
			all["gene"] = gene
			all["beg"] = beg
			all["end"] = end
			all["strand"] = strand
			
			genomelist.append(all)

print(json.dumps(genomelist, indent=4))
"""
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
