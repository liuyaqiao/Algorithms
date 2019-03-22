# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxVal = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.maxVal
        
    def helper(self, root):
        ## return 以root为根节点的最长univalue path
        
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if root.left != None and root.val == root.left.val:
            left += 1
        else:
            left = 0
            
        if root.right != None and root.val == root.right.val:
            right += 1
        else:
            right = 0
        
        self.maxVal = max(self.maxVal, left + right)
        
        return max(left, right)
        