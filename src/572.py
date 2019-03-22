# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None:
            return t is None
        if s.val == t.val and self.isSame(s,t) == True:
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSame(self, s, t):
        if s == None:
            return t is None
        if t == None:
            return False
        if s.val != t.val:
            return False
        else:
            return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        
'''
主要的关注点是
对于s是否为None的判断
'''