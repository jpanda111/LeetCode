# -*- coding: utf-8 -*-
"""
Created on Fri May 11 13:34:19 2018

@author: yinjiang
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

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
def numJInS(J,S,n):
    if (n==1):
        return sum(map(J.count, S)) # slowest
    elif(n==2):
        return sum(map(S.count, J)) #similar to mine
    elif(n==3):
        return sum(s in J for s in S) # similar to mine
    elif(n==4):
        setJ = set(J)
        return sum(s in setJ for s in S)
    else:
        r = 0
        for item in J:
            if item in S:
                r += S.count(item)
        return r

# my solution    
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # brunte force
        r = 0
        for item in J:
            if item in S:
                r += S.count(item)
        return r
    
# others

#return sum([{x: 1 for x in J}.get(x, 0) for x in S])
#return sum(map(J.count, S))
#return sum(mpa(S.count, J))
#return sum(s in J for s in S)
#Explanation
'''
read J and build jewels hash set.
read S and count jewels.
Time complexity
I used hash set and it's O(1) to check if it contains an element.
So the total time complexity will be O(M+N), instead of O(MN)
'''
# using hash set
# setJ=set(J); return sum(s in setJ for s in S)
# using bitset by Java
'''
BitSet bitSet = new BitSet(J.length)
for (char j: J.toCharArray()) {
    bitSet.set(j)
    }
'''
                