# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root == None:
            return []
        result = []
        stack = [root]
        
        while stack:
            level = []
            for i in range(len(stack)):
                t = stack.pop(0)
                level.append(t.val)
                if t.left != None:
                    stack.append(t.left)
                if t.right != None:
                    stack.append(t.right)
            result.append(level)
        result.reverse()
        return result