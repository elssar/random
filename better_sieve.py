#!/usr/bin/env python

# Sieve of Eratosthenes - to find all the prime numbers in range 1 to n
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Optimized by only putting in 2, 3 & numbers of the form 6n+/-1 in the initial list.

def better_sieve(n):
	primes = []
	numbers = []
	if 2<=n:
		primes.append(2)
		if 3<=n:
			primes.append(3)
	for i in range(1, n/6 +1):
		numbers.append(6*i-1)
		numbers.append(6*i+1)
	while numbers:
		primes.append(numbers.pop(0))
		for e in numbers:
			if not e%primes[-1]:
				numbers.pop(numbers.index(e))
	return primes

def is_prime(n):
	prime_list = better_sieve(n)
	if n in prime_list:
		return True
	return False

if __name__=='__main__':
	print '1. Print Sieve, 2. Check primalarity, 3. Sum :(Option Number)'
	c= raw_input()
	inp= c.split()
	try:
		assert len(inp)==2
		if inp[0]=='1':
			if inp[1].isdigit():
				print better_sieve(int(inp[1]))
			else:
				raise Exception('Incorrect input')
		elif inp[0]=='2':
			if inp[1].isdigit():
				print is_prime(int(inp[1]))
			else:
				raise Exception('Incorrect input')
		elif inp[0]=='3':
		    if inp[1].isdigit():
		        print sum(better_sieve(int(inp[1])))
		    else:
		        raise Exception('Incorrect input')
		else:
			raise Exception('Incorrect input')
	except:
		print 'Invalid input!'
