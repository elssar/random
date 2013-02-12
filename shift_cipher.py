#!/usr/bin/python

# Shift cipher

def shift_cipher(plain_text, shift_coeff):
	cipher_text= ''
	for c in plain_text:
		cipher_text+= 32 if ord(c)==32 else chr(65+ (ord(c)-65+shift_coeff%26)%26)
	return cipher_text

if __name__=='__main__':
	s= ['THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 'TO BE OR NOT TO BE THAT IS THE QUESTION', 'THERE IS NO SPOON', 'DONT PANIC AND CARRY A TOWEL',
	    'THE CAKE IS A LIE']
	c= [3, 5, 7, 29, 19]
	for p, n in zip(s,c):
		print 'plain_text= "'+p+'"'
		print 'shift_coeff=',n
		print 'cipher_text=', shift_cipher(p, n)
