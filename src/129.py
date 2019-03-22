# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
        
    def dfs(self, root, depth):
        # return sum with root and depth, depth means level
        if root == None:
            return 0
        
        sum = root.val + 10 * depth
        
        if root.left == None and root.right == None:
            return sum
        
        return self.dfs(root.left, sum) + self.dfs(root.right, sum)
    
'''
首先树的题要使用一个先序遍历，先处理根节点，再处理左右子树；
第二要考虑根节点和left，right有什么关系：
这里的关系是：
总的sum = 10 * 前一层的和 + root.val


'''