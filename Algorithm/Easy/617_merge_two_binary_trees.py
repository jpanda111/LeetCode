# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:28:12 2018
@author: yinjiang

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
"""
import time
def timeit(func):
    def wrapper(*args):
        t = time.clock()
        res = func(*args)
        print "The time to run the function: '%s' is %s seconds" %(func.func_name, time.clock()-t)
        return res
    return wrapper

class Solution(object):
    @timeit
    def mergeTrees(self,t1,t2, n):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if (n==1):# recursion pre-order
            if not t1 and not t2: return None
            if not t1:
                return t2
            if not t2:
                return t1
            r=TreeNode(t1.val+t2.val)
            r.left=self.mergeTrees(t1.left,t2.left)
            r.right=self.mergeTrees(t1.right,t2.right)
            return r
        if (n==2):# recursion in-order
            if not t1 and not t2: return None
            if not t1:
                return t2
            if not t2:
                return t1
            tLeft = self.mergeTrees(t1.left,t2.left)
            r=TreeNode(t1.val+t2.val)
            r.left= tLeft
            r.right=self.mergeTrees(t1.right,t2.right)
            return r   
        if (n==3):# recursion post-order
            if not t1 and not t2: return None
            if not t1:
                return t2
            if not t2:
                return t1
            tLeft = self.mergeTrees(t1.left,t2.left)
            tRight = self.mergeTrees(t1.right,t2.right)
            r=TreeNode(t1.val+t2.val)
            r.left, r.right= tLeft, tRight
            return r 
        if (n==4): # iterative pre-order
            if not t1 and not t2: return None
            if not t1:
                return t2
            if not t2:
                return t1
            stack1 = [t1]
            stack2 = [t2]
            tRoot = TreeNode(t1.val+t2.val)
            stack = [tRoot]
            while len(stack)>0:
                t1=stack1.pop()
                t2=stack2.pop()
                t=stack.pop()
                if t1.right is None and t2.right is None:
                    pass
                elif t1.right is None:
                    t.right = t2.right
                elif t2.right is None:
                    t.right = t1.right
                else:
                    t.right = TreeNode(t1.right.val +t2.right.val)
                    stack1.append(t1.right)
                    stack2.append(t2.right)
                    stack.append(t.right)
                if t1.left is None and t2.left is None:
                    pass
                elif t1.left is None:
                    t.left = t2.left
                elif t2.left is None:
                    t.left = t1.left
                else:
                    t.left = TreeNode(t1.left.val+t2.left.val)
                    stack1.append(t1.left)
                    stack2.append(t2.left)
                    stack.append(t.left)
            return tRoot
        if (n==5): #Iterative in-order
            if not t1 and not t2: return None
            if not t1:
                return t2
            if not t2:
                return t1
            
            stack1=[]
            stack2=[]
            stack=[]
            tRoot=TreeNode(t1.val+t2.val)
            t=tRoot
            while len(stack1)>0 or t1 is not None:
                while t1 is not None and t2 is not None:
                    stack1.append(t1)
                    stack2.append(t2)
                    stack.append(t)
                    if t1.left is not None and t2.left is not None:
                        t.left=TreeNode(t1.left.val+t2.left.val)
                        t=t.left
                    t1,t2=t1.left,t2.left
                if t1 is not None:
                    t.left=t1
                if t2 is not None:
                    t.left=t2
                t1,t2,t=stack1.pop(),stack2.pop(),stack.pop()
                if t1.right is None and t2.right is None:
                    t1=t2=None
                elif t1.right is None:
                    t.right=t2.right
                    t1=t2=None
                elif t2.right is None:
                    t.right=t1.right
                    t1=t2=None
                else:
                    t.right=TreeNode(t1.right.val+t2.right.val)
                    t1,t2,t=t1.right,t2.right,t.right
            return tRoot
        
        if (n==6): #BFS
            from collections import deque
            if t1 is None and t2 is None:
                return None
            if t1 is None:
                return t2
            if t2 is None:
                return t1
            q1,q2,q=deque(),deque(),deque()
            tRoot=TreeNode(t1.val+t2.val)
            t=tRoot
            q1.append(t1)
            q2.append(t2)
            q.append(t)
            while len(q1)>0:
                t1,t2,t=q1.popleft(),q2.popleft(),q.popleft()
                if t1.left is None and t2.left is None:
                    pass
                elif t1.left is None:
                    t.left=t2.left
                elif t2.left is None:
                    t.left=t1.left
                else:
                    t.left=TreeNode(t1.left.val+t2.left.val)
                    q1.append(t1.left)
                    q2.append(t2.left)
                    q.append(t.left)
                if t1.right is None and t2.right is None:
                    pass
                elif t1.right is None:
                    t.right = t2.right
                elif t2.right is None:
                    t.right = t1.right
                else:
                    t.right = TreeNode(t1.right.val+t2.right.val)
                    q1.append(t1.right)
                    q2.append(t2.right)
                    q.append(t.right)
            return tRoot                  

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''    
Complexity Analysis of Recursion Approach

Time complexity : O(m). A total of m nodes need to be traversed. 
Here, m represents the minimum number of nodes from the two given trees.
Space complexity : O(m). The depth of the recursion tree can go up 
to m in the case of a skewed tree. In average case, depth will be O(logm).

Complexity Analysis of Iterative Approach

Time complexity : O(n). We traverse over a total of n nodes. 
Here, n refers to the smaller of the number of nodes in the two trees.
Space complexity : O(n). The depth of stack can grow up to n in case of a skewed tree.



'''    

        
