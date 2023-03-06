# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome

import mcb185
import argparse

#CLI input
parser = argparse.ArgumentParser(description ='ORF finder')

parser.add_argument('file', type=str, metavar='<path>', help='somefile')
parser.add_argument('--orf', required=False, type=int, default=300,
	metavar='<int>', help='optional orf min. size [default=%(default)i]')

arg = parser.parse_args()

sample = 'GCGATGCTGATGCTGATCGTATAACCCATGCAGGCGATGCTGATGCTGATCGTATAACCCATGCAG'

#Reverse DNA Function
def reverse(parent):
	rseq = ''
	for i in range(len(parent)):
		if parent[i] == 'A': rseq += 'T'
		elif parent[i] == 'C': rseq += 'G'
		elif parent[i] == 'G': rseq += 'C'
		elif parent[i] == 'T': rseq += 'A'
		else: rseq += 'X'
	return rseq


#ORF using protein
def orf_p(protein):
	orf = False
	locations = {}
	for i in range(len(protein)):

		if not orf:
			if protein[i] != 'M':
				#print(i, protein[i], 'n')
				continue
			else:
				start = (i + 1) * 3 - 2
				orf = True
		
		if orf:
			#print(i, protein[i], 'e')
			if protein[i] == '*':
				locations[start] = (i + 1) * 3
				orf = False
		
	return(locations)

#ORF using DNA
def orf(seq):
	i = 0
	orf = False
	locations = {}
	
	while i < len(seq):
		codon = seq[i:i+3]
		
		#Find a start codon
		if not orf:
			if codon != 'ATG':
				#print(i, codon)
				i += 1
			else:
				orf = True
				start = i
		
		#Find a stop codon
		if orf:
			end = False
			if codon == 'TAA': end = True
			elif codon == 'TAG': end = True
			elif codon == 'TGA' : end = True
			else:
				#print(i, codon, 'y')
				i += 3
			
			if end:
				#print(i, codon)
				locations[start + 1] = i + 3
				orf = False
				i += 3
	return locations

print(orf(sample))
print(orf_p(mcb185.translate(sample)))

listy = orf(sample)

for item in listy:
	print(item, listy[item])





"""
for defline, seq in mcb185.read_fasta(arg.file):
	words = defline.split()
	name = words[0]
	seqorf = orf(seq)


	
	#print(orf_p(mcb185.translate(seq)))
	print(orf(seq))
"""
"""
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""
