# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None:
            return None
        return self.buildNode(nums, 0, len(nums) - 1)
    
    def buildNode(self, nums, left, right):
        if left > right:
            return None
        
        node = TreeNode(nums[(left + right)//2])
        node.left = self.buildNode(nums, left, (left + right)//2 - 1)
        node.right = self.buildNode(nums, (left + right) // 2 + 1, right)
        
        return node

