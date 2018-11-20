# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
#         if root == None:
#             return []
#         res = []
#         self.tranverse(root, res)
#         return res
        
        
#     def tranverse(self, root, res):
#         if root == None:
#             return
        
#         res.append(root.val)
#         self.tranverse(root.left, res)
#         self.tranverse(root.right, res)
        if root == None:
            return []
        
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right != None:
                stack.append(node.right)      
            if node.left != None:
                stack.append(node.left)

        return res
        