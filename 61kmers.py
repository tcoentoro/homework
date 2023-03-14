# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()

import argparse
import mcb185

parser = argparse.ArgumentParser(description='Kmer Count for a Fasta File')

parser.add_argument('file', type=str, metavar='<path>', help='somefile')
parser.add_argument('--ks', required=False, type=int, default=1,
	metavar='<int>', help='optional kmer size [default=%(default)i]')

arg = parser.parse_args()

for defline, seq in mcb185.read_fasta(arg.file):
	seq = seq.upper()
	kmers = {}
	
	for i in range(0, len(seq) - arg.ks + 1):
		kmer = seq[i:i + arg.ks]

		if kmer not in kmers:
			kmers[kmer] = 0
		kmers[kmer] += 1

for j in range(len(kmers)):
	kmer_list = []
	kmer_list += kmers.keys()

kmer_list.sort()

for keyss in kmer_list:
	print(keyss, kmers[keyss])



#question: do i need to sort it every after iteration?
#are kmers supposed to overlap? (overlap = answer below, no overlap = diff ans)
#how to sort a dictionary?
#what should I do with the remainder nucleotide?
"""
python3 60kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
