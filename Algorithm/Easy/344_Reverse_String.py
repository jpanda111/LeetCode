# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:37:46 2018
@author: yinjiang

Write a function that takes a string as input and returns the string reversed.
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
def reverseString(s,n):
    if (n==1):#pythonic
        return s[::-1]
    if (n==2):#classic
        r = list(s)
        i, j = 0, len(r)-1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1
        return "".join(r)
    if (n==3):#recursive question?
        l = len(s)
        if l < 2:
            return s
        return reverseString(s[1/2:],3)+reverseString(s[:1/2],3)
    if (n==4):
        for i in range(n/2):
            s[i], s[~i] = s[~i], s[i]
        return "".join(s)
    if (n==5):
        return "".join(reversed(list(s)))
    
class Solution(object):# question?
    def reverseString1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        n=len(s)
        return self.reverseString1(s[n//2:])+self.reverseString1(s[:n//2])