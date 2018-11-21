# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return None
        if pNode.right != None:
            return self.FindLeftOfTree(pNode.right)
        else:
            temp = pNode.next
            while temp != None and temp.right == pNode:
                pNode = temp
                temp = pNode.next
            return temp
    def FindLeftOfTree(self, pNode):
        while pNode.left != None:
            pNode = pNode.left
        return pNode
    