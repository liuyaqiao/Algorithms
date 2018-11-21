# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        
        newNode = ListNode(-1)
        head = newNode
        
        while pHead1 != None and pHead2 != None:
            if pHead1.val < pHead2.val:
                newNode.next = pHead1
                pHead1 = pHead1.next
                newNode = newNode.next
            else:
                newNode.next = pHead2
                pHead2 = pHead2.next
                newNode = newNode.next
        if pHead1 == None:
            newNode.next = pHead2
        if pHead2 == None:
            newNode.next = pHead1
            
        return head.next