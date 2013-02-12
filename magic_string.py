#!/usr/bin/python

from better_sieve import better_sieve

def combi(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

string= "jnovujepzpzfctucvehrzzkjxmzclmbachzqoxurybbkzrjuxysbhklfclwe"

#alphabets= range(1, 27)
m= 0

for char in string:
    m+= ord(char)%96
    
primes= better_sieve(m)
maxs= 0
longs= ''

#for seq in combi(alphabets, 4):
#    if sum(seq) in primes:
#        s+= sum(seq)

#print s

for window in xrange(1, len(string)):
    for clip in xrange(len(string)-window+1):
        s= 0
        subs= string[clip:clip+window]
        for char in subs:
            s+= ord(char)%96
        if s in primes and s>maxs:
            maxs= s
            longs= string[clip:clip+window]

print s, longs, len(longs)
