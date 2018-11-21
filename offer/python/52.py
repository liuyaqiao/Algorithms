# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        length1, length2 = 0, 0
        temp1, temp2 = pHead1, pHead2
        while temp1 != None:
            temp1 = temp1.next
            length1 += 1
        while temp2 != None:
            temp2 = temp2.next
            length2 += 1
        
        if length1 > length2:
            for i in range(length1 - length2):
                pHead1 = pHead1.next
        else:
            for i in range(length2 - length1):
                pHead2 = pHead2.next
        
        while True:
            if pHead1 == None or pHead2 == None:
                return None
            if pHead1.val == pHead2.val:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next