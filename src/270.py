# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = 0
    gap = float('inf')
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return 0
        self.tranverse(root, target)
        return self.result
        
    def tranverse(self, root, target):
        if not root:
            return
        
        temp = abs(root.val - target)
        if temp < self.gap:
            self.gap = temp
            self.result = root.val
        
        self.tranverse(root.left, target)
        self.tranverse(root.right, target)