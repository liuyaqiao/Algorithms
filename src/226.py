# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        temp = left
        root.left = root.right
        root.right = temp
        
        return root

'''
divide and conquer 更简单的一道题：

注意的地方有两个：

1. 明确left、right的含义
2. 注意return的值

'''