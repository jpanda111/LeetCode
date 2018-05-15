# -*- coding: utf-8 -*-
"""
Created on Sun May 13 18:01:43 2018
@author: yinjiang

We are to write the letters of a given string S, from left to right into lines. 
Each line has maximum width 100 units, and if writing a letter would cause the 
width of the line to exceed 100 units, it is written on the next line. 
We are given an array widths, an array where widths[0] is the width of 'a', 
widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S, 
and what is the width used by the last such line? 
Return your answer as an integer list of length 2.

Example :
Input: 
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
Output: [3, 60]
Explanation: 
All letters have the same length of 10. To write all 26 letters,
we need two full lines and one line with 60 units.

Example :
Input: 
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
Output: [2, 4]
Explanation: 
All letters except 'a' have the same length of 10, and 
"bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units.
For the last 'a', it is written on the second line because
there is only 2 units left in the first line.
So the answer is 2 lines, plus 4 units in the second line.

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
def numberOfLines(widths, S, n):
    if (n==1):
        l = [ord(s)-ord('a') for s in S]
        ans = 0
        line = 1
        m = len(l)
        for i in range(m):
            ans += widths[l[i]]
            if ans < 100:
                continue
            elif ans == 100:
                line += 1
                ans = 0
            else:
                line += 1
                ans = widths[l[i]]
        return [line,ans]
    if (n==2):
        line, ans = 1,0
        if S: return None
        for s in S:
            width = widths[ord(s)-ord('a')]
            line +=1 if ans+width > 100 else 0
            ans = width if ans+width > 100 else ans+width
        return [line, ans]
    if (n==3):
        ans = 0
        line = 1
        for s in S:
            ans += widths[ord(s)-ord('a')]
            if ans > 100:
                ans = widths[ord(s)-ord('a')]
                line += 1
        return [line, ans]
    if (n==4):
        import string
        widths_dict = dict(zip(string.ascii_lowercase, widths))
        count = 0
        lines = 0
        for s in S:
            count += widths_dict[s]
            if count > 100:
                lines += 1
                count = widths_dict[s]
            elif count == 100:
                lines += 1
                count = 0
        return [lines+1, count]
    
            
        