# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        fast = head
        slow = head
        
        while True:
            if fast == None or fast.next == None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        fast = head
        
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
        