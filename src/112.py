# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        return self.dfs(root, sum)
    
    
    def dfs(self, root, sum):
        if root == None:
            return
        if root.val == sum and root.left == None and root.right == None:
            return True
  
        self.dfs(root.left, sum - root.val)
        self.dfs(root.right, sum - root.val)
        
        # return False
        
        