#!/usr/bin/python

# New Sieve - Trying to improve the Sieve of Eratosthenes

def better_sieve(n):
	numbers= []
	primes= []
	if n>=2:
		primes.append(2)
		if n>=3:
			primes.append(3)
	for i in range(6, n/6+1, 6):
		numbers.append(i-1)
		numbers.append(i+1)
	while numbers:
		
	return primes
			
prime= better_sieve(10000)
#print prime
print len(prime)
