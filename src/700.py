# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        while root != None:
            
            if root.val == val:
                return root
            elif val > root.val:
                root = root.right
            else:
                root = root.left
            
        return None
        
        
        