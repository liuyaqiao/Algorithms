# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.leaves = []
        self.tree_height(root)
        return self.leaves
        
    def tree_height(self, root):
        if root == None:
            return -1
        left = self.tree_height(root.left)
        right = self.tree_height(root.right)
        
        height = 1 + max(left, right)
        if height >= len(self.leaves):
            self.leaves.append([])
        self.leaves[height].append(root.val)
        return height
            

'''
用height作为数组的index来取元素；

'''