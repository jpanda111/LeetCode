# -*- coding: utf-8 -*-
"""
Created on Sun May 13 17:08:50 2018
@author: yinjiang

Given an array of 2n integers, group these integers into n pairs of integer, 
makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
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
def arrayPairSum(nums,n):
    if (n==1):# sort based solution
        temp=sorted(nums)
        return sum([temp[i] for i in range(0,len(nums),2)])
    if (n==2):
        return sum(sorted(nums)[::2])
    if (n==3):# hash based solution
        '''
        1. run through all nums once and keep record of found digit in hash. 
        So, if the number is found twice then hash[number+10000] = 2 . 
        build the frequency map for the input.
        (have to plus 10000 here because index start at 0 but num in[-10000,10000])
        2. run through that hash[-10000,10000],skip number that does not in the list 
        if(hash[i]==0). so we are sure that the lesser number would be processed first
        3. p is a toggle button or a switch. The concept is to pick minimum, skip next 
        minimum, pick next minimum, skip next....Inside while loop, when frequency is 
        even, the contribution is implied number times freq//2, when odd, it is implied
        number times (freq//2+1)
        '''
        bucket = [0]*20001
        for n in nums:
            bucket[n+10000] +=1
        res=0
        p=0
        for i in range(20001):
            if bucket[i] == 0:
                continue
            while bucket[i] != 0:# keep looping until go through all the duplicate's
                if p % 2 == 0:
                    res += i-10000 # only pick even ones
                p += 1
                bucket[i] -= 1
        return res
    if (n==4):
        res = [0]*20001
        for x in nums:
            res[x+10000] += 1
        s_so_far, adjust = 0, False
        for idx, freq in enumerate(res):
            if freq:
                freq = freq-1 if adjust else freq
                if freq & 1:
                    s_so_far += ((freq//2)+1)*(idx-10000)
                    adjust = True
                else:
                    s_so_far += ((freq//2))*(idx-10000)
                    adjust = False
        return s_so_far
            