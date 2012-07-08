#!/usr/bin/env python
#
# Will find collataz numbers for a set number of hours, and then store them in a text file - collatz.txt

import time
from os import getcwd

collatz_sequence = [1]             # initialize the list with 1
time_to_run = float(raw_input())   # in hours
start_time = time.time()
end_time = start_time+time_to_run*60*60     # time when the loop ends, in seconds
while time.time()<=end_time:                
	temp_list = []
	i = collatz_sequence[-1]+1
	while i!=1:
	    temp_list.append(i)
	    if i%2:
	    	i = 3*i+1
	    else:
	    	i = i/2
	    if i in collatz_sequence:
			break
	collatz_sequence = collatz_sequence + temp_list
	collatz_sequence.sort()
f = open(getcwd()+'collatz.txt','w')
f.write('Total values : ' + str(len(collatz_sequence))+'\n')
f.write('Highest value : ' + str(collatz_sequence[-1]) + '\n')
f.write('Digits in highest value : ' + str(len(str(collatz_sequence[-1]))) + '\n')
f.write('Start sequence\n')
f.write('______________\n')    # 14 '_'s + 1 new line = 15 chars.
for i in collatz_sequence:
	f.write(str(i)+',')
f.close()
print len(collatz_sequence)
print collatz_sequence[-1]
print len(str(collatz_sequence[-1]))
