#!/usr/bin/python

# Program to check whether all the words of a sentence are Python keywords to help with
# this faux Code Golf question - Write the longest sentence using keywords of a programming language
# http://codegolf.stackexchange.com/questions/9422/write-the-longest-sentence-using-keywords-of-a-programming-language

from keyword import kwlist
from re import findall

def kwcheck(sentence):
    """Check whether all the words of a sentence are Python keywords"""
    words= findall(r'\w+', sentence)
    for word in words:
        if word.lower() not in kwlist:
            return False
    return True, len(words)
    
if __name__ == '__main__':
    sen= raw_input("Enter your sentence: ")
    print kwcheck(sen)
