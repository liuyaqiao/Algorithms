# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = []
        path = []
        self.helper(root, sum, path, result)
        return result
    
    def helper(self, root, sum, path, result):
        #return a list meets requirement
        if root == None:
            return 
        #condition
        if root.left == None and root.right == None and root.val == sum:
            path.append(root.val)
            result.append(path)
            return
        