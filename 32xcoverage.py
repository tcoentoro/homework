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

#ReSequencing Depth Tally
coverage0 = []

for i in range(gsize): # <-- sequence length
	coverage0.append(0)

for j in range(rnum): # <-- number of reads
	nucnum = random.randint(0, gsize - rlen)
	
	for k in range(rlen): # <-- length of read
		coverage0[nucnum + k] += 1

#Undersample Removal
coverage = []
cutoff = 5

for depth in coverage0:
	if depth >= cutoff: coverage.append(depth)
	
#Stats Calculations
minimum = min(coverage)
maximum = max(coverage)
total = sum(coverage)
average = total/len(coverage)

#Output
print(f'{minimum} {maximum} {average:.5f}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
