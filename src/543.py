# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxVal = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxdepth(root)
        return self.maxVal
    
    def maxdepth(self, root):
        if not root:
            return 0
        left = self.maxdepth(root.left)
        right = self.maxdepth(root.right)
        
        self.maxVal = max(self.maxVal, left + right)
        
        return max(left, right) + 1

'''
求最大直径，使用最大depth的算法，用一个全局变量来储存
最大直径。

全局变量在树中经常用到。
'''