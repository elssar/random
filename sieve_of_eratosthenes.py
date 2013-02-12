#!/usr/bin/env python

# Sieve of Eratosthenes - to find all the prime numbers in range 1 to n
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def sieve_of_eratosthenes(n):
	primes = []
	numbers = []
	for i in range(2, n+1):
		numbers.append(i)
	while numbers:
		primes.append(numbers.pop(0))
		for e in numbers:
			if not e%primes[-1]:
				numbers.pop(numbers.index(e))
	return primes

def is_prime(n):
	prime_list = sieve_of_eratosthenes(n)
	if n in prime_list:
		return True
	return False

if __name__=='__main__':
	print '1. Print Sieve, 2. Check primalarity :(Option Number), 3. Sum'
	c= raw_input()
	inp= c.split()
	try:
		assert len(inp)==2
		if inp[0]=='1':
			if inp[1].isdigit():
				print sieve_of_eratosthenes(int(inp[1]))
			else:
				raise Exception('Incorrect input')
		elif inp[0]=='2':
			if inp[1].isdigit():
				print is_prime(int(inp[1]))
			else:
				raise Exception('Incorrect input')
		elif inp[0]=='3':
		    if inp[1].isdigit():
		        print sum(sieve_of_eratosthenes(int(inp[1])))
		    else:
		        raise Exception('Incorrect input')
		else:
			raise Exception('Incorrect input')
	except:
		print 'Invalid input!'
