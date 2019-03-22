# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        head = ListNode(-1)
        prev = head
        curt1 = l1
        curt2 = l2
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next                
            else:
                head.next = l2
                head = head.next
                l2 = l2.next
        
        if l1 == None:
            head.next = l2
        if l2 == None:
            head.next = l1
        
        return prev.next
        


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        