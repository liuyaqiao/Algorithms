# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return 
        dummy = ListNode(-1)
        dummy.next = head
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None
        
        newhead = self.reverse(slow)
        
        self.merge(head, newhead)
        
        
        
    def reverse(self, head):
        if not head:
            return None
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
            
        return prev
        
    def merge(self, l1, l2):
        while l1 and l2:
            post_l1 = l1.next
            l1.next = l2
            l1 = post_l1
            if l1 == None:
                break
            post_l2 = l2.next
            l2.next = l1
            l2 = post_l2

            
'''
brute force解法：

需要注意：

1. reverse， merge等基本操作的写法
2. merge中要考虑有一方等于None的写法
3. 把指针从中间分开的写法

'''
        