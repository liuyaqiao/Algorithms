# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    tilt = 0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root)
        return self.tilt
    
    def helper(self, root):
        # return current sum with this root
        if root == None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        self.tilt += abs(left - right)
        return root.val + left + right

