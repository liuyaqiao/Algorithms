# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        prev = None
        while pHead != None:
            temp = pHead
            pHead = pHead.next
            temp.next = prev
            prev = temp
        return prev