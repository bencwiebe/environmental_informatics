#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:20:06 2022

@author: benjaminwiebe
"""

"""
The following functions allow for 1) printing something twice, 2) executing a function
with a given argument twice and 3) executing a function with a given argument four times,
using the function that executes a function twice. This provides good practice on 
embedding functions in other functions.
"""
#define function which executes any function "func" twice using the same argument, "arg"
def do_twice(func, arg):
    func(arg)
    func(arg)

#define function which prints any argument "arg" twice.
def print_twice(arg):
    print(arg)
    print(arg)

#define function which executes an argument four times. This is accomplished by calling
#on the function "do_twice" two times.
def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)



# the following condition checks whether we are running as a
# script (like when you test the code), in which case run the
# test code, or being imported (say by the autograder), in
# which case don't.  Your main code should be "indented"
# within this conditional, just like the example code.

if __name__ == '__main__':


    # start by making this work (and adding your own comments)
    do_twice(print, 'spam')

    # then make this statement work (do not forget to remove the #)
    do_twice(print_twice, 'spam')

    # finally, make this statement work
    do_four(print_twice, 'spam')
    
    
    
    
    
    
    
    
    
    
    