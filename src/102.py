# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root == None:
            return []
        
        res = []
        stack = [root]
        
        while stack:
            level = []
            for i in range(len(stack)):
                temp = stack.pop(0)
                # level = []
                level.append(temp.val)
            
                if temp.left != None:
                    stack.append(temp.left)
                if temp.right != None:
                    stack.append(temp.right)
            res.append(level)   
        return res
            