#!/usr/bin/python
# 
# Random Walk
# Rather, it should be called drunkards walk. Our drunk is standing 100 meters from his house & in the opposite direction a cliff lies at a
# distance of 110 meters. He can walk either backwards or forwards. This program will calculate wether our drunk reaches home, or falls off the cliff
# and in how many steps.

import random

def randomwalk(home=0, pos=100, cliff=210):
	'Random walk in one dimension.'
	random.seed()
	count= 0
	while True:
		if random.random()<0.5:
			pos-= 1
		else:
			pos+= 1
		count+= 1
		if pos==home:
			return [True, count]
		elif pos==cliff:
			return [False, count]

if __name__=='__main__':
	print randomwalk()
