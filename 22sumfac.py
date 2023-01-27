# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

import math

n = 5 # use this value for your computation
rsum= 0
for i in range(n):
	rsum += i+1
print(n, rsum, math.factorial(n))

"""
python3 22sumfac.py
5 15 120
"""