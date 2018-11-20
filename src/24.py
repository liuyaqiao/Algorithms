# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        #pre->1->2->3->4
        preHead = ListNode(-1)
        preHead.next = head
        
        curt = preHead
        
        
        
        while curt.next != None and curt.next.next != None:
            ##head != None 可以保证curt.next != None
            self.SwapTwoNode(curt)
            curt = curt.next.next
            
        return preHead.next
            
        
        
        
    def SwapTwoNode(self, prev):
        #input is pre Node, return is is the same Node
        #prev->1->2->NULL
        #prev->1->None
        
        #prev->1->2->NULL
        curt = prev.next
        post = curt.next
        
        prev.next = post
        curt.next = post.next
        post.next = curt
        
        return prev