#!/usr/bin/env python
#
# I'm bored, so a program to see if two numbers are anagrams.

def check_if_anagram(x, y):
	a = []
	b = []
	while x>0 and y>0:
		a.append(x%10)
		b.append(y%10)
		x = x/10
		y = y/10
	if x>0 or y>0:
		return 0
	a.sort()
	b.sort()
	if a==b:
		return 1
	else:
		return 0


x = int(raw_input())
y = int(raw_input())
if check_if_anagram(x,y):
	print 'Same digits'
else:
	print 'Different digits'
