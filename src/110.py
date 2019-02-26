# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        left = self.depth(root.left)
        right = self.depth(root.right)
        
        return (abs(left - right) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def depth(self, root):
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        
        return max(left, right) + 1

'''
balanced binary tree

可以用resulttype的形式

'''