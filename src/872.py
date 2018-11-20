# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        result = []
        result2 = []
        self.getLeaves(root1, result)
        self.getLeaves(root2,result2)
        
        if result == result2:
            return True
        return False
        
    
    def getLeaves(self, root, result):
        if root == None:
            return
        if root.left == None and root.right == None:
            result.append(root.val)
        
        self.getLeaves(root.left, result)
        self.getLeaves(root.right, result)
        