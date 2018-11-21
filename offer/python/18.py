# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead

        start = ListNode(-1)
        start.next = pHead
        prev = start

        while pHead != None:
            next = pHead.next
            ifDeleted = False

            if next != None and pHead.val == next.val:
                ifDeleted = True

            if ifDeleted == False:
                prev = pHead
                pHead = pHead.next

            if ifDeleted == True:
                val = pHead.val
                while pHead != None and pHead.val == val:
                    pHead = pHead.next
                if pHead == None:
                    prev.next = pHead
                    #return start.next
                else:
                    prev.next = pHead
        return start.next                    
                   
        