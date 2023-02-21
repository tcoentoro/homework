# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import sys
import mcb185
import math

wsize = int(sys.argv[2])
thres = float(sys.argv[3])

#seq = 'AGTCGAGTCGACCCCCCCCGTGGATGCT'
#seq_l = list(seq)

#Amino Acid Entropy Calculator
def nucentropy(seq):
	
	nuc = 'ACGT'
	tally = [0] * 4
	ent = 0
	
	for i in range(len(seq)):
		tally[nuc.find(seq[i])] += 1/len(seq)
	
	for val in tally:
		if val == 0: continue
		ent += -(val * math.log2(val))
	
	return ent

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	seql = list(seq)
	
	for i in range(len(seq) - wsize + 1):
		window = seq[i:i + wsize]
		
		if nucentropy(window) < thres: seql[i] = 'N'
		
	seq = ''.join(seql)

for j in range(0, len(seq), 60):
	print(seq[j:j + 60])

"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
