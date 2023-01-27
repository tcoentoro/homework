# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers
import random

length = 30
countAT = 0
dna = ''

for i in range(length):
	r = random.randint(1,6)
	if 		r == 1 or r == 2: nt = 'A'
	elif 	r == 3 or r == 4: nt = 'T'
	elif 	r == 5			: nt = 'C'
	else					: nt = 'G'
	
	dna += nt
	if nt == 'A' or nt == 'T' : countAT += 1
	

print(length, countAT/length, dna)


"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
