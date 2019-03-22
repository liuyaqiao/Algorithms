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
        
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        
        if root.left == None and root.right == None:
            return sum == root.val
        
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


'''
分别用了divide and conquer 和 tranverse方法

重点去别就是：

divide conquer的返回值和原来的函数相同；而tranverse一般没有返回值
'''