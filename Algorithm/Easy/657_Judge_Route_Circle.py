# -*- coding: utf-8 -*-
"""
Created on Fri May 11 18:44:48 2018
@author: yinjiang
Initially, there is a Robot at position (0, 0). 
Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.
The move sequence is represented by a string. 
And each move is represent by a character. 
The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
The output should be true or false representing whether the robot makes a circle.
"""
import time
import collections
def timeit(func):
    def wrapper(*args):
        t = time.clock()
        res = func(*args)
        print "The time to run the function: '%s' is %s seconds" %(func.func_name, time.clock()-t)
        return res
    return wrapper
@timeit
def judgeCircle(moves, n):
        """
        :type moves: str
        :rtype: bool
        """
        if (n==1):
            return (moves.count("U") == moves.count("D")) & (moves.count("R") == moves.count("L"))
        elif (n==2):
            u,d,l,r = map(moves.count, "UDLR")
            return u==d and l==r
        elif (n==3):
            c = collections.Counter(moves)
            return c['L']==c['R'] and c['U']==c['D']
        elif (n==4):
            return not sum(1j**'RUL'.find(m) for m in moves)
        elif (n==5):
            x=y=0
            for m in moves:
                if m == 'U': y-=1
                elif m == 'D': y +=1 
                elif m == 'L': x -=1
                elif m == 'R': x +=1
            return x == y == 0
'''
n=5 solution
Complexity Analysis
Time Complexity: O(N), where N is the length of moves. We iterate through the string.
Space Complexity: O(1).
'''