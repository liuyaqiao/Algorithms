# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code hereclass Solution:
        if head == None:
            return None 
        if k == 0:
            return None
        p1, p2 = head, head
        for i in range(k - 1):
            if p1.next != None:
                p1 = p1.next
            else:
                return None
        
        while p1.next != None:
            p2 = p2.next
            p1 = p1.next
            
        return p2