# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if root.val >= L and root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
        
        if root.val < L:
            return self.trimBST(root.right, L, R)
            
            
        if root.val > R:
            return self.trimBST(root.left, L, R)
            
'''
divide and conquer

需要考虑每次分完之后的left和right与 root之间的关系

并且在对返回值的类型各种条件要明确清楚。

'''
            
