# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

#Input
numbers = []

for num in sys.argv[1:]:
	numbers.append(float(num))

numbers.sort() 


#Calculations: Total + mean
total = sum(numbers)
mean = total/len(numbers)
mid = len(numbers) // 2


#Calculations: Median
median = None

if len(numbers) % 2 == 0:
	median = (numbers[mid] + numbers[mid-1])/2
else:
	median = numbers[mid]


#Calculations: Standard Deviation
sumdistance = 0

for x in numbers:
	sumdistance += (x - mean) ** 2
	
sd = (sumdistance/len(numbers)) ** 0.5


#Output
print(f'Count: {len(numbers)}')
print(f'Minimum: {numbers[0]:.1f}')
print(f'Maximum: {numbers[-1]:.1f}')
print(f'Mean: {(mean):.3f}')
print(f'Std. dev: {sd:.3f}')
print(f'Median {median:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
