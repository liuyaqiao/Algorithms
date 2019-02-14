# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: 'int') -> 'List[TreeNode]':
        if n == 0:
            return []
        return self.generateTreesList(1, n)
    
    def generateTreesList(self, start, end):
        if start > end:
            return [None]
        
        res = []
        
        for i in range(start, end + 1):
            left = self.generateTreesList(start, i - 1)
            right = self.generateTreesList(i + 1, end)
            
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
                    
        return res
            
        
'''
这是96题的follow up，对于这种找出全部答案的题目，我们要考虑使用dfs来做：




'''