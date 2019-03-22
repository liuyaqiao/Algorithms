# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) != 0:
            root = TreeNode(-1)
            val = max(nums)
            index = nums.index(val)
            root.val = val
            root.left = self.constructMaximumBinaryTree(nums[:index])
            root.right = self.constructMaximumBinaryTree(nums[index + 1:])
            return root
        else:
            return None

'''


'''