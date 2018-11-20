# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0

        result = []
        
        self.dfs(root, result)

        return sum(result)
        
    def dfs(self, root, result):
        if root.left != None and root.left.left == None and root.left.right == None:
            result.append(root.left.val)
    
        if root.left != None:
            self.dfs(root.left, result)
        if root.right != None:
            self.dfs(root.right, result)