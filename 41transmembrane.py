# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane

import sys
import mcb185
import random

#Function for Kyle-Dolittle Hydrophobicity
def kd_hydrop(aa):
	hydrop = 0

	aas = 'ACDEFGHIKLMNPQRSTVWY'
	aas_hs = [1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6, -3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3]
	
	hydrop += aas_hs[aas.find(aa)]
	return hydrop

#Function for Average Hydrophobicity in a window
def ave_hydrop(window):
	total_hydrop = 0
	
	for i in range(len(window)):
		total_hydrop += kd_hydrop(window[i])
	
	average = total_hydrop/len(window)
	return average

#Filtering though data
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	name = words[0]

	speptide = 8
	kd_peptide = 2.5
	signal = False
	
	ahelix = 11
	kd_ahelix = 2.0
	ahelix_nyeh = False
	
	cutoff = 30
	#Signal Peptide
	for j in range(len(seq[:cutoff]) - speptide):
		seq_win1 = seq[j:j + speptide]
		
		if 'P' in seq_win1: continue
		elif ave_hydrop(seq_win1) < kd_peptide: continue
		else:
			signal = True
			break
	
	#Hydrophobic Region
	if signal:
		for k in range(len(seq[cutoff:]) - ahelix):
			seq_win2 = seq[k + cutoff:k + cutoff + ahelix]
			
			if 'P'in seq_win2: continue
			if ave_hydrop(seq_win2) < kd_ahelix: continue
			else:
				ahelix_nyeh = True
				break
	
	if ahelix_nyeh:
		print(name, defline)
		#print(seq_win1, ave_hydrop(seq_win1))
		#print(seq_win2, ave_hydrop(seq_win2))	










"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
