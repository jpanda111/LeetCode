# -*- coding: utf-8 -*-
"""
Created on Fri May 11 15:57:55 2018

@author: yinjiang
International Morse Code defines a standard encoding 
where each letter is mapped to a series of dots and dashes, 
"a" maps to ".-", "b" maps to "-...", "c" maps to "-.-."
Given a list of words, each word can be written as a concatenation of the Morse code of each letter.
Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

"""
l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

import time
def timeit(func):
    def wrapper(*args):
        t = time.clock()
        res = func(*args)
        print "The time to run the function: '%s' is %s seconds" %(func.func_name, time.clock()-t)
        return res
    return wrapper
@timeit
def UniqueMorseWord(words, n):
    if (n==1):
        res = set()
        for word in words:
            val=""
            for s in word:
                val+=l[ord(s)-ord('a')]
            res.add(val)
        return len(res)
    # Transform each word into it's Morse Code representation. 
    # We put all transformations into a set seen, and return the size of the set.
    elif (n==2):
        return len({''.join(l[ord(i) - ord('a')] for i in w) for w in words})
    else:
        l1 = []
        for items in words:
            s = ''
            for item in items:
                s+=l[ord(item)-ord('a')]
            l1.append(s)
        return len(set(l1))
            
## Official solution
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)
#Complexity Analysis
#Time Complexity: O(S), where SS is the sum of the lengths of words in words. We iterate through each character of each word in words.
#Space Complexity: O(S).            
        
    