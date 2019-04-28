"""
Problem ID : 1
link : https://projecteuler.net/problem=1 
"""

def eid_1():
	"""
	Multiples of 3 and 5:
	If we list all the natural numbers below 10 that are multiples of 3 or 5, 
	we get 3, 5, 6 and 9. The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000.
	"""

	N=1000 # search ceiling

	vals=[]
	sum = 0 

	for num in range(1, N):
		if (num % 3 == 0) or (num % 5 == 0):
			sum=sum+num
			vals.append(num)
	result = sum
	return result