# -*- coding: utf-8 -*-
"""
Created on Tue May 15 08:36:33 2018
@author: yinjiang

Given a positive integer, output its complement number. The complement 
strategy is to flip the bits of its binary representation.
1. The given integer is within the range of a 32-bit signed integer.
2. no leading zero bit in the integer’s binary representation.
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), 
and its complement is 010. So you need to output 2.
"""

def timeit(func):
    import time
    def wrapper(*args):
        t = time.clock()
        res = func(*args)
        print "The time to run the function: '%s' is %s seconds" %(func.func_name, time.clock()-t)
        return res
    return wrapper
@timeit
def findComplement(num,n):
    if (n==1):
        s = ''
        while num > 0:
            s += str(1-num%2)
            num = num/2
        return int(s[::-1],2)
    if (n==2):
        i = 1
        while i <= num:
            i = i << 1
        return (i-1)^num