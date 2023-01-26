# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
rdna = dna[::-1]
for i in range(len(rdna)):
	if rdna[i] == 'A' : cdna = 'T'
	if rdna[i] == 'T' : cdna = 'A'
	if rdna[i] == 'C' : cdna = 'G'
	if rdna[i] == 'G' : cdna = 'C'
	print(cdna, end = "")


"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
