# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:27:03 2018
@author: yinjiang

A website domain like "discuss.leetcode.com" consists of various subdomains. 
At the top level, we have "com", at the next level, we have "leetcode.com", 
and at the lowest level, "discuss.leetcode.com". When we visit a domain like 
"discuss.leetcode.com", we will also visit the parent domains "leetcode.com" 
and "com" implicitly.

call a "count-paired domain" to be a count (representing the number of visits 
this domain received), followed by a space, followed by the address. 
An example of a count-paired domain might be "9001 discuss.leetcode.com".

Example 1:
Input: 
["9001 discuss.leetcode.com"]
Output: 
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation: 
We only have one website domain: "discuss.leetcode.com". As discussed above, 
the subdomain "leetcode.com" and "com" will also be visited. 
So they will all be visited 9001 times.

Example 2:
Input: 
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: 
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org",
"1 intel.mail.com","951 com"]
Explanation: 
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, 
"intel.mail.com" once and "wiki.org" 5 times. For the subdomains, 
we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, 
and "org" 5 times.


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
def subdomainVisits(cpdomains, n):
    if (n==1):
        visit = {}
        subdomain = []
        for item in cpdomains:
            count, domain = item.split()
            count = int(count)
            subdomain = domain.split('.')
            for i in xrange(len(subdomain)):
                names = ".".join(subdomain[i:])
                if names in visit:
                    visit[names] += count
                else:
                    visit[names] = count
        l = []
        for s in visit:
            temp = str(visit[s]) + " " + str(s)
            l.append(temp)
        return l
        #return ["%d %s" % (d,t) for t, d in visit.items()]
    if (n==2): # hash map
        # using collections instead of dictionary
        ans = collections.Counter()
        for item in cpdomains:
            count, domain = item.split()
            count = int(count)
            subdomain = domain.split('.')
            for i in xrange(len(subdomain)):
                ans[".".join(subdomain[i:])] += count
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
    if (n==3):
        dropFirst = lambda d: re.sub('[^\.]*\.','', d, 1)
        getNext = lambda d: dropFirst(d) if dropFirst(d) != d else None
        counter = {}
        for item in cpdomains:
            c, d =  item.split(' ')
            while d is not None:
                counter[d] = counter.get(d, 0) + int(c)
                d = getNext(d)
                print d
        return [str(c) + ' ' + d for d,c in counter.items()]
    if (n==4): # use defaultdict instead of regular dict
        '''
         standard dictionary includes the method setdefault() for retrieving a 
         value and establishing a default if the value does not exist. 
         By contrast, defaultdict lets the caller specify the default up 
         front when the container is initialized.
         It can be especially useful if the default is a type used for 
         aggregating or accumulating values, such as a list, set, or even int.
        '''
        counts = collections.defaultdict(int) ## make the value type int
        for item in cpdomains:
            c, domain = item.split()
            c = int(c)
            while '.' in domain:# use while loop instead of for loop
                counts[domain] += c
                domain = domain.split('.', 1)[1]
            else:
                counts[domain] += c
        return ['%d %s' %(v,k) for k,v in counts.items()]
        