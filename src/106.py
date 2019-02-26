# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder or len(inorder) != len(postorder) :
            return None
        
        root = TreeNode(postorder[-1])
        rootindex = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:rootindex], postorder[:rootindex])
        root.right = self.buildTree(inorder[rootindex+1:], postorder[rootindex:len(postorder) - 1])
        
        return root
