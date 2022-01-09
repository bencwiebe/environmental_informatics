#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:56:52 2022

@author: benjaminwiebe
"""

"""
This is an exercise in making a grid print out on the screen. This utilizes several "for"
loops which allow for rather quick editing, should the user ever want a grid other than
4x4.
"""

#define function which prints a 4x4 grid. Does not take any arguments.
def print_grid():
    #print horizontal rows of grid one at a time
    for n in range(4):
        #print top line of each row
        for i in range(4):
            print("+ ", end="")
            print("- - - - ", end="")
        print("+")
        
        #print sides of columns for the row
        for i in range(4):
            print("|         |         |         |         |")
        
    #print bottom line of bottom row
    print("+ - - - - + - - - - + - - - - + - - - - +")
        
    
    

# the following condition checks whether we are running as a
# script (like when you test the code), in which case run the
# test code, or being imported (say by the autograder), in
# which case don't.  Your main code should be "indented"
# within this conditional, just like the example code.

if __name__ == '__main__':

    # make this statement produce a 4x4 grid on the screen
    print_grid()
    
    
    
    