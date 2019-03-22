# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
        
    def helper(self, root, sum):
        # return number of tree with root and sum
        res = 0
        if root == None:
            return res
        if root.val == sum:
            res += 1
        res = res + self.helper(root.left, sum - root.val) + self.helper(root.right, sum - root.val)
        return res

'''
用了两个dfs，主要的关键点：
1. 要知道helper函数的具体的含义和返回值
2. 在主函数中，要确保结果等于三个部分的和。
'''