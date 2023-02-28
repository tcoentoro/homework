#!/usr/bin/env python3
# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. the entropy of each window is centered (N's in the middle of windows)
# 2. has option and default value for window size
# 3. has option and default value for entropy threshold
# 4. has a switch for N-based or lowercase (soft) masking
# 5. works with uppercase or lowercase input files
# 6. works as an executable

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

import mcb185
import math
import argparse

# setup
parser = argparse.ArgumentParser(description='Nucleotide Entropy Filter')

# positional argument(file)
parser.add_argument('file', type=str, metavar='<path>', help='somefile')

# Optional Values(Window Size, Entropy threshold)
parser.add_argument('--ws', required=False, type=int, default=10,
	metavar='<int>', help='optional window size [default = %(default)in]')
parser.add_argument('--en', required=False, type=float, default=1.0,
	metavar='<float>', help='optional entropy threshold [default = %(default)i]')
parser.add_argument('--wr', required=False, type=int, default=60,
	metavar='<int>', help='optional character wrap [default = %(default)i characters]')

# switch
parser.add_argument('--mask', action='store_true', help='N-base/lowercase masking')


arg = parser.parse_args()

#Entropy Filtering Program
def nucentropy(seq):
	
	nuc = 'ACGT'
	tally = [0] * 4
	ent = 0
	
	for i in range(len(seq)):
		tally[nuc.find(seq[i])] += 1
	
	for val in tally:
		if val == 0: continue
		ent += -(val * math.log2(val/len(seq)))/len(seq)
	
	return ent

for defline, seq in mcb185.read_fasta(arg.file):
	seq = seq.upper()
	seql = list(seq)
	
	for i in range(len(seq) - arg.ws + 1):
		window = seq[i:i + arg.ws]
		
		h = nucentropy(window)
		
		if nucentropy(window) < arg.en:
			for j in range(len(window)):
				if arg.mask:
					seql[i + j] = 'N'
				else:
					seql[i + j] = seq[i + j].lower()
		#print(window, h)
	seq = ''.join(seql)

for k in range(0, len(seq), arg.wr):
	print(seq[k:k + arg.wr])


"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""
