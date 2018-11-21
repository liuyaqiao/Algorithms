# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        self.exchange(root)
        return root
    
    def exchange(self, root):
        if root == None:
            return 
        
        left = self.exchange(root.left)
        right = self.exchange(root.right)
        
        temp = root.right
        root.right = root.left
        root.left = temp