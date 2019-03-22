# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        prev = root
        while True:
            if root.val < val:
                if root.right == None:
                    root.right = TreeNode(val)
                    break
                else:
                    root = root.right
                    
            else:
                if root.left == None:
                    root.left = TreeNode(val)
                    break
                else:
                    root = root.left
            
        return prev

        