# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot == None or k == 0:
            return None
        result = []
        self.inOrderRec(pRoot, result)
        if k > len(result):
            return None
        return result[k - 1]
    
    def inOrderRec(self, pRoot, result):
        if pRoot == None:
            return 
        
        self.inOrderRec(pRoot.left, result)
        result.append(pRoot)
        self.inOrderRec(pRoot.right, result)  