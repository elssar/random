#!/usr/bin/python

# A program to simulate Integer Overflow, and prove a point
# http://www.udacity.com/wiki/CS101%20Homework%202?course=cs101 - Q5

def int_overflow(n):
    maxint= 2**16-1
    minint= -2**16
    i= 1
    while True:
        i*= 2
        if i>maxint:
            i= minint + (i-maxint)
        elif i<minint:
            i= maxint + (i-minint)
        n+=1
        if n>maxint:
            n= minint + (n-maxint)
        if i>n:
            print "Breaking at n=", n, "and i=", i
            break

n= int(raw_input())
int_overflow(n)
