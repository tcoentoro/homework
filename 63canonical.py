# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein


import argparse
import re
import gzip
import mcb185

parser = argparse.ArgumentParser(description = 'ATG Finder RegEx')
parser.add_argument('file', type=str, metavar='<path>', help='genomic bank file')
arg = parser.parse_args()

sequence = ""

#will ignore any pseudogenes
with gzip.open(arg.file, 'rt') as fp:
	for line in fp:
		if line.startswith('ORIGIN'):
			break
	for line in fp:
		f = line.split()
		sequence += "".join(f[1:])

#print(len(sequence))

with gzip.open(arg.file, 'rt') as fp:
	for line in fp:
		for match in re.finditer('\s(CDS)\s', line):
			
			coor = re.search('(\d+)\.\.(\d+)', line)
			beg = int(coor.group(1))
			end = int(coor.group(2))
			
			if 'complement' in line:
				nyeh = mcb185.reverse(sequence[end-3:end])
			
			#print(sequence[beg-1:beg+2])
			#if 'complement' in line:
			#print(line, coor.group(1),)


"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
