# -*- coding: utf-8 -*-
"""
Created on Mon May 14 18:53:51 2018
@author: yinjiang

defaultdict vs dict vs OrderedDict: depends on the following:
    - Size of the data set;
    - Number of unique keys;
    - Speed of the underlying factory for defaultdict;
    - Speed of OrderDict vs some later ordering step;
    - Version of Python.
setdefault is faster and simpler with small data sets
defaultdict is faster for larger data sets with more homogenous key sets;
setdefault has an advantage with more heterogeneous key sets;
OrderedDict is slower in all cases other than an algorithm that depends on 
order and order is not easy to reconstruct or sort;
"""

from __future__ import print_function
from collections import defaultdict
from collections import OrderedDict

try:
    t=unichr(100)
except NameError:
    unichr=chr
    
def f1(li):
    '''defaultdict'''
    d = defaultdict(list)
    for k, v in li:
        d[k].append(v)
    return d.items()

def f2(li):
    '''setdefault'''
    d={}
    for k, v in li:
        d.setdefault(k, []).append(v)
    return d.items()

def f3(li):
    '''OrderedDict'''
    d=OrderedDict()
    for k, v in li:
        d.setdefault(k, []).append(v)
    return d.items() 

if __name__ == '__main__':
    import timeit
    import sys
    print(sys.version)
    few=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    fmt='{:>12}: {:10.2f} micro sec/call ({:,} elements, {:,} keys)'
    for tag, m, n in [('small',5,10000), ('medium',20,1000), ('bigger',1000,100), ('large',5000,10)]:
        for f in [f1,f2,f3]:
            s = few*m
#            print(s)
            res=timeit.timeit("{}(s)".format(f.__name__), setup="from __main__ import {}, s".format(f.__name__), number=n)
            st=fmt.format(f.__doc__, res/n*1000000, len(s), len(f(s)))
#            print(res)
            print(st)
            s = [(unichr(i%0x10000),i) for i in range(1,len(s)+1)]
            res=timeit.timeit("{}(s)".format(f.__name__), setup="from __main__ import {}, s".format(f.__name__), number=n)
            st=fmt.format(f.__doc__, res/n*1000000, len(s), len(f(s)))
            print(st)            
        print() 