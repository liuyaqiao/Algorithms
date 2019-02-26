# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:rootindex + 1], inorder[0:rootindex])
        root.right = self.buildTree(preorder[rootindex + 1 : ], inorder[rootindex + 1:])
        return root