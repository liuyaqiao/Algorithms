# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        #divide and conquer
        if root == None:
            return 0
        
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        
        depth = min(leftDepth, rightDepth) + 1
        
        if root.left == None:
            return rightDepth + 1
        if root.right == None:
            return leftDepth + 1
        
        return depth
        