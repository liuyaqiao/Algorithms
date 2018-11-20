# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        
        depth = max(leftDepth, rightDepth) + 1
        
        return depth