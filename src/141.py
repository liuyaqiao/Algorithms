# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        quick = head
        slow = head
        
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                return True
        return False