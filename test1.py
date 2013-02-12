#!/usr/bin/env python
# Command line argument test

from sys import argv
from os import getcwd, path
from functools import wraps

class Test:
    def __init__(self):
        self.name= 'woot'
        self.meh= []
        self.fun= {}
    def args(self):
        return argv
    def Parse(self, function):
        if function:
            @wraps(function)
            def wrap():
                function()
                print 'Ha!'
            self.fun[`wrap`]= wrap
            return wrap   
        else:
            self.meh.append('pfft')
    def Execute(self):
        for bleh in self.fun:
            self.fun[bleh]()

def return_path():
    #return path.abspath(argv[0])
    #return getcwd()
    return argv[0]
