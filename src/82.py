# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return None
        
        preHead = ListNode(-1)
        preHead.next = head
        pre = preHead
        tmp = head
        while pre.next != None and pre.next.next != None:
            if pre.next.val == pre.next.next.val:
                sameNums = pre.next.val
                while pre.next != None and pre.next.val == sameNums:
                    pre.next = pre.next.next
            else:
                pre = pre.next
                
        return preHead.next
                