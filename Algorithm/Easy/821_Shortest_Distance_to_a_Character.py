# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:55:10 2018
@author: yinjiang

Given a string S and a character C, return an array of integers representing
the shortest distance from the character C in the string.
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
"""

import re
def split(delimiters, string, maxsplit = 0):
    # delimiters = "."," "
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)
import collections
def timeit(func):
    import time
    def wrapper(*args):
        t = time.clock()
        res = func(*args)
        print "The time to run the function: '%s' is %s seconds" %(func.func_name, time.clock()-t)
        return res
    return wrapper
@timeit
def shortestToChar(S,C,n):
    if (n==1):
        import numpy
        temp = numpy.array([i for i, letter in enumerate(S) if letter == C])
        return [min(abs(temp-i)) for i in range(len(S))]
    if (n==2):
        temp = [i for i, letter in enumerate(S) if letter == C]
        l = []
        for k in range(len(S)):
            a=[abs(temp[j]-k) for j in range(len(temp))]
            l.append(min(a))
        return l
    if (n==3): 
        '''
        initial result array res, loop twice on S, first loop find shortest
        distance to character on left, second loop find shortest distance to
        character on right
        '''
        m = len(S)
        res = [m] * m
        pos = -m # make sure pos initial number is big enough
        for i in range(m) + range(m)[::-1]:
            if S[i]==C:
                pos = i
            res[i] = min(res[i], abs(i-pos))
        return res
    if (n==4):
        '''
        first loop to find all C and initialize distance to 0
        the rest is the same as above n==3
        '''
        m = len(S)
        res = [0 if c == C else m for c in S]
        for i in range(m-1):
            res[i+1] = min(res[i+1], res[i]+1)
        for i in range(m-1)[::-1]:
            res[i] = min(res[i], res[i+1]+1)
        return res
    if (n==5): #BFS
        m = len(S)
        res = [0] * m
        queue = collections.deque()
        for i in range(m):
            if S[i] == C:
                queue.append(i)
                res[i] = 0
            else:
                res[i] = -1
        level = 0
        while queue:
            level += 1
            for i in range(len(queue)):
                index = queue.popleft()
                for j in [1, -1]:
                    idx2 = index + j
                    if 0 <= idx2 <= m-1 and res[idx2] == -1:
                        queue.append(idx2)
                        res[idx2] = level
        return res
    if (n==6):
        '''
        only loop once, before find the first C, just calculate the distance
        from 2nd C coming, decide which one to use, last or current, based on 
        result, pick the closest, divide by 2 and calculate accordingly
        '''
        size, last = len(S), -1
        res = []
        for i in range(size):
            if S[i] != C:
                continue
            if not res:
                res += list(range(i, -1, -1))
            else:
                res += list(range(1, (i-last+1)//2)) + list(range((i - last) // 2, -1, -1))
            last = i
        return res + list(range(1, size-last))
    