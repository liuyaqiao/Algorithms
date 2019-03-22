# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        self.tranverse(root, result)
        return result
    
    def tranverse(self, root, result):
        if not root:
            return
        
        self.tranverse(root.left, result)
        self.tranverse(root.right, result)
        
        result.append(root.val)