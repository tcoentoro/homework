# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input

#Libraries
import sys
import math


#Input
vals = []

for val in sys.argv[1:]:
	try:
		p = float(val)
	except:
		raise ValueError(f'cannot convert "{val}" to a number')
	vals.append(float(val))

#Total prob = 1
total_1 = sum(vals)

try:
	assert(math.isclose(total_1, 1.0))
except:
	raise ValueError(f'The sum of your probabilities is not 1')

#Calculations
entropy = 0

for j in vals:
	entropy += -(j * math.log2(j))

#Output
print(f'{entropy:.3f}')


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
