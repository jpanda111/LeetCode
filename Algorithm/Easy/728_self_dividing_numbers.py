# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:51:13 2018
@author: yinjiang
A self-dividing number is a number that is divisible by every digit it contains.
128 is a self-dividing number because 128 % 1==0, 128 % 2==0, and 128 % 8==0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, 
output a list of every possible self dividing number, 
including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
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
def selfDividingNumbers(left,right,n):
    if (n==1):
        out=[]
        for i in range(left,right+1):
            l=str(i)
            t=True
            if '0' in l:
                continue
            for item in l:
                if i%int(item)!=0:
                    t=False
                    break
            if t:
                out.append(i)
        return out
    if (n==2):
        return [num for num in range(left, right+1) if not any(item =='0' or num % int(item) !=0 for item in str(num))]
    if (n==3):
        out = lambda num: '0' not in str(num) and all([num%int(item)==0 for item in str(num)])
        return filter(out,range(left,right+1))
    if (n==4): # using generator, allow for short-circuit evaluation, so all will terminate as soon as one failed
        out = lambda num: '0' not in str(num) and all( num%int(item)==0 for item in str(num))
        return filter(out,range(left,right+1))
    if (n==5): # brute force algorithm
        result=[]
        for num in range(left, right+1):
            if is_self_dividing(num):
                result.append(num)
        return result
    if (n==6):
        result=[]
        for num in range(left, right+1):
            if selfDividingHelper(num):
                result.append(num)
        return result
    if (n==7):
        ans=[]
        for i in range(left, right+1):
            for j in str(i):
                if j=='0' or i % int(j) != 0:
                    break
            ans.append(i)
    if (n==8):
        result = []
        for i in range(left, right+1):
            check=True
            temp = i
            while temp !=0:
                if temp % 10 ==0:
                    check=False
                    break
                elif i % (temp%10) !=0:
                    check=False
                    break
                temp=temp/10
            if check==True:
                result.append(i)
        return result
            
def is_self_dividing(num):
    s=str(num)
    for d in s:
        if d=='0' or num % int(d) !=0:
            return False
    return True
def selfDividingHelper(num):
    temp = num
    while temp:
        if not temp % 10 or num%(temp%10):
            return False
        temp = temp//10
    return True
            