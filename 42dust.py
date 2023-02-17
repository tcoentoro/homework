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

win_size = 8
e_thres = 0

seq = 'AGTCGAGTCGACCCCCCCCGTGGATGCT'

#Entropy Calculator
def entropy(seq):
	
	aas = 'ACGT'
	tally = [0] * 4
	ent = 0
	
	for i in range(len(seq)):
		tally[aas.find(seq[i])] += 1/len(seq)
	
	for val in tally:
		if val == 0: continue
		ent += -(val * math.log2(val))

	return ent

#Largest AA counter
def aa_max(seqq):
	
	aas = 'ACGT'
	tally = 
	
	for i in range(len(seqq)):
		tally[aas.find(seqq[i])] += '1'
	
	return aas[tally.find]

found = False


for j in range(len(seq) -  win_size + 1):
	win = seq[j:j + win_size]
	
	if entropy(win) <= e_thres:
		found = True
		print(win, entropy(win), 'yep')
		break
	else:
		print(win, entropy(win), 'nop')

print(seq)



"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	name = words[0]
	print(name, seq)
"""


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
