# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return None
        pQuick, pSlow = pHead, pHead
        
        while True:
            if pQuick == None or pQuick.next == None:
                return None
            
            pQuick = pQuick.next.next
            pSlow = pSlow.next
            
            if pQuick == pSlow:
                break
        while pHead != pQuick:
            pHead = pHead.next
            pQuick = pQuick.next
        return pHead
                