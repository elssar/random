#!/usr/bin/env python
#
# Will make a 2D spiral array
# The problem is defined here - http://rosettacode.org/wiki/Spiral_matrix
# Meh, here goes absolutely nothing.

def make_spiral(n):
	spiral= []
	for i in range(n):
		spiral.append([])
		for j in range(n):
			spiral[i].append(None)
	maxi=maxj=n-1
	mini=minj=i=j=0
	for c in range(1, n*n+1):
		spiral[i][j]= c
		#print c, i, j, mini, minj, maxi, maxj
		if i==mini and j<maxj:
			j+= 1
		elif j==maxj and i<maxi:
			i+= 1
		elif i==maxi and j>minj:
			j-= 1
		elif j==minj and i>mini:
			i-= 1
		if i==maxi and j==maxj:
			mini+= 1
		elif i==maxi and j==minj:
			maxj-= 1
		elif i==mini and j==minj:
			maxi-= 1
		elif i==mini and j==maxj and mini>0:
			minj+= 1
	return spiral

if __name__=='__main__':
	print 'Enter range(>0):'	
	try:
		n= raw_input()
		if not n.isdigit():
			raise Exception('Invalid input')
		if int(n)==0
		for i in range(1, int(n)):
			s= make_spiral(i)
			for r in s:
				print r
	except:
		print 'Invalid input!'
