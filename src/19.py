# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        preHead = ListNode(-1)
        preHead.next = head
        pre = preHead
        
        postPointer = head

        for i in range(n):
            postPointer = postPointer.next
              
        while postPointer != None:
            head = head.next
            postPointer = postPointer.next
            pre = pre.next
        pre.next = head.next
        
        return preHead.next