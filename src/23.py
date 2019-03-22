# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.sort(lists, 0, len(lists) - 1)
        
    def sort(self, lists, left, right):
        if left >= right:
            return lists[left]
        
        mid = left + (right - left) // 2
        
        l1 = self.sort(lists, left, mid)
        l2 = self.sort(lists, mid + 1, right)
        
        return self.merge(l1, l2)
        
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
用分治的方法来解决，在对于每一个链表的处理中又用了merge
merge操作也是递归比较简单。

'''