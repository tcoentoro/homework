# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
count = 0
countcg = 0

for i in range(len(dna)-1):
	count += 1
	if dna[i] == 'C' or dna[i] == 'G': countcg += 1
	if count == len(dna)-1 :
		print(f'{(countcg/len(dna)):.2f}')

"""
python3 24gc.py
0.42
"""