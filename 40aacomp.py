# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use 20 named variables
# Variation: use a list

import sys
import gzip

fp = gzip.open(sys.argv[1], 'rt')
aas = 'ACDEFGHIKLMNPQRSTVWY'
tally = [0]*len(aas)

for line in fp.readlines():
	if line.startswith('>'): continue
	line.rstrip()

	for aa in aas:
		for aaprotein in line:
			if aaprotein == aa: tally[aas.find(aa)] += 1

totalaa = sum(tally)

for i in range(len(aas)):
	print(f'{aas[i]} {tally[i]} {tally[i]/totalaa:.4f}')

fp.close()



"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""
