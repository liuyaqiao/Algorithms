# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dummy = TreeNode(-1)
        self.prev = self.dummy
        self.helper(root)
        return self.dummy.right
    
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.prev.right = root
        self.prev = root
        self.prev.left = None       
        self.helper(root.right)