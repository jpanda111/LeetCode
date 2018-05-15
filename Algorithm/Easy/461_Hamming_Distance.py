# -*- coding: utf-8 -*-
"""
Created on Fri May 11 17:33:31 2018
@author: yinjiang

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Example:
Input: x = 1, y = 4
Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
       
# Python Bitwise Operators
a = 0011 1100
b = 0000 1101
-----------------
a&b = 0000 1100
a|b = 0011 1101
a^b = 0011 0001
~a  = 1100 0011

& Binary AND	
Operator copies a bit to the result if it exists in both operands	
(a & b) (means 0000 1100)

| Binary OR	
It copies a bit if it exists in either operand.	
(a | b) = 61 (means 0011 1101)

^ Binary XOR	
It copies the bit if it is set in one operand but not both.
(a ^ b) = 49 (means 0011 0001)

~ Binary Ones 
Complement	It is unary and has the effect of 'flipping' bits.	
(~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.

<< Binary 
Left Shift	The left operands value is moved left by the number of bits specified by the right operand.	
a << 2 = 240 (means 1111 0000)

>> Binary 
Right Shift	The left operands value is moved right by the number of bits specified by the right operand.	
a >> 2 = 15 (means 0000 1111)
"""

import time
def timeit(func):
    def wrapper(*args):
        t = time.clock()
        res = func(*args)
        print "The time to run the function: '%s' is %s seconds" %(func.func_name, time.clock()-t)
        return res
    return wrapper
@timeit
def hammingDistance(x,y,n):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    if (n==1):
        return bin(x^y).count('1')
    elif (n==2):#second fatest
        z = x^y
        ans = 0
        while z > 0:
            ans += z % 2 # result on current bit value, 0 or 1
            z >>= 1 # right shift = divide by 2, remainder
        return ans # sum up all the 1's
    elif (n==3):
        xOR = x^y
        s = bin(xOR)
        return sum(char == '1' for char in s)
    elif (n==4):# slowest
        xbin, ybin = bin(x)[2:], bin(y)[2:]
        nfill = max(len(xbin), len(ybin))
        xout = 0
        for i in zip(xbin.zfill(nfill), ybin.zfill(nfill)):
            # zip is a list of tuples, test if the same using set
            if len(set(i)) > 1:
                xout += 1
    elif (n==5): #fastest
        x = x^y
        y = 0
        while x:
            y += 1
            x = x & (x-1)
        return y
    elif (n==6):
        ans = 0
        while x or y:
            ans += (x%2) ^ (y%2)
            x /= 2
            y /= 2
        return ans