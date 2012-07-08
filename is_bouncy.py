#!/usr/bin/python

# Bouncy or not

def is_bouncy(n):
	if n<100:
		return False
	lst= []
	for d in str(n):
		lst.append(d)
	fwd= lst[:]
	rev= fwd[:]
	fwd.sort()
	rev.sort(reverse=True)
	if lst==fwd or lst==rev:
		return False
	return True

if __name__=='__main__':
	print 'Enter positive number':
	try:
		n= raw_input()
		if not n.isdigit():
			raise Exception('Invalid input')
		print is_bouncy(int(n))
	except:
		print 'Invalid input!'
