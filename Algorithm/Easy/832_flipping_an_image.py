# -*- coding: utf-8 -*-
"""
Created on Sun May 13 14:45:16 2018
@author: yinjiang
Given a binary matrix A, we want to flip the image horizontally, then invert 
it, and return the resulting image.To flip an image horizontally means that 
each row of the image is reversed.To invert an image means that each 0 is 
replaced by 1, and each 1 is replaced by 0. 

Example 1:
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
"""

import time
#import collections
def timeit(func):
    def wrapper(*args):
        t = time.clock()
        res = func(*args)
        print "The time to run the function: '%s' is %s seconds" %(func.func_name, time.clock()-t)
        return res
    return wrapper
@timeit
def flipAndInvertImage(A,n):
    if (n==1):
        return [[1^i for i in reversed(l)] for l in A] # reverse list using l[::-1] but much slower than reversed() function
    if (n==2):
        return [map(lambda b: 1^b, reversed(l)) for l in A] # use map
    if (n==3):
        return [[1-i for i in reversed(l)] for l in A] # ^ bitwise operator much slower than 1-i
    if (n==4): # more readable style
        flip = []
        m=len(A)
        # for i,l in enumerate(A): # i is the index and l is the content
        for i in range(m):
            flip.append([]) 
            for j in range(m):# reverse list
                flip[i].append(1-A[i][m-1-j])
        return flip
            
        