# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        prev, fast, slow = None, head, head 
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2        
        
'''
用归并排序比较方便，需要注意的地方有两个：

1. 要找到当前链表的中点
2. 写一个merge的函数
3. 中点的的地方要断开，next = None

'''
