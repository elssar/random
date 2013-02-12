#!/usr/bin/env python
#
# Will generate a random PIN

"""
Generate a random PIN
usage -
generate_pin.py <n>
*n - number of digits required. Optional, defaults to 4 if not given
"""

from string import digits
from random import choice
from sys import argv

def genpin(n=4):
    return ''.join(choice(digits) for i in range(n))

if __name__=='__main__':
    if len(argv)==1:
        print genpin()
    elif len(argv)==2 and argv[1].isdigit():
        print genpin(int(argv[1]))
    else:
        print __doc__