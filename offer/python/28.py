# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.isSymmetricalRec(pRoot, pRoot)
    def isSymmetricalRec(self, lRoot, rRoot):
        if lRoot == None and rRoot == None:
            return True
        if lRoot == None or rRoot == None:
            return False
        if lRoot.val != rRoot.val:
            return False
        
        return self.isSymmetricalRec(lRoot.left,rRoot.right) and self.isSymmetricalRec(lRoot.right, rRoot.left)
        