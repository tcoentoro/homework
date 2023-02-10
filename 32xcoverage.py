# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

import sys
import random

#Input
vals = []

for val in sys.argv[1:]:
	vals.append(int(val))	

gsize = vals[0]
rnum = vals[1]
rlen = vals[2]



"""
#Nucleotide Generators
genome = []

for i in range(gsize): # <-- Genome
	nuc = random.choice('ACGT')
	genome.append(nuc)


for j in range(rnum): # <-- Reads
	nucnum = random.randint(0, gsize - rlen)
	
	for k in range(rlen):

#output
print(f'Genome: {genome}')
"""


#Template
coverage = []

for i in range(gsize): # <-- sequence length
	coverage.append(0)

for j in range(rnum): # <-- number of reads
	nucnum = random.randint(0, gsize - rlen)
	
	for k in range(rlen):
		coverage[nucnum + k] += 1
	
	print(f'Read {j + 1}: Position {nucnum + 1} ')

print('---------')
print(f'Coverage: {coverage}')
print(f'Geonome Size: {gsize} nucleotides')
print(f'Read Number: {rnum}')
print(f'Read Length: {rlen}')



'''
#test can i add stuff to a list

haha = [0, 0, 0, 0]

for i in range(3):
	haha[i] += 1

print(haha)
'''

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
