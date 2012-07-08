#!/usr/bin/python

# Program to calculate the Collatz of each number from 1 to n

import math
import time

def collatz(n, cg):
	if n in cg:
		return
	if math.log(n, 2)==int(math.log(n, 2)):
		cg[n]= [int(2**(math.log(n,2)-1)), int(math.log(n, 2))]
		collatz(2**(math.log(n,2)-1), cg)
		return
	else:
		if n%2:
			c= 3*n+1
		else:
			c= n/2
		collatz(c, cg)
		cg[n]= [c, cg[c][1]+1]
		return
	
def calc_cycle(n):
	collatz_graph= {1: [None, 0]}
	for i in range(2,n+1):
		if i not in collatz_graph:
			collatz(i, collatz_graph)
	return collatz_graph

if __name__=='__main__':
	t= time.time()	
	coll_g= calc_cycle(1000000)
	longest_cycle= [1, [None, 0]]
	for num in coll_g:
		if coll_g[num][1]>longest_cycle[1][1] and num<=1000000:
			longest_cycle= [num, coll_g[num]]		
	print longest_cycle
	print time.time()-t
