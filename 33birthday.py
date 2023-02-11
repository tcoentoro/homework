# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import sys
import random


#List Formation
vals = []

for val in sys.argv[1:]:
	vals.append(float(val))

print(vals)

#Calculations
trials = 10000 # <-- How many times do you want to run it?
ppl = int(vals[1])
days = vals[0]
num_matches = 0

#loop for number of trial runs
for l in range(trials):
	bdays = []
	match = False
	
	#loop to generate list of birthdates
	for i in range(ppl):
		date= random.randint(1, days)
		bdays.append(date)
	
	#loop for birthdate 1
	for j in range(len(bdays)):
		
		#loop for birthdate 2
		for k in range(j+1, len(bdays)):
			if bdays[j] == bdays[k]:
				match = True;
				break

		if match:
			num_matches += 1;
			break
			

prob = num_matches/trials

print(prob)

"""
python3 33birthday.py 365 23
0.571
"""

