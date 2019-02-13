2.# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        if head == None:
            return None
        
        smallHead = ListNode(-1)
        largeHead = ListNode(-1)
        small = smallHead
        large = largeHead
        
        while head != None:
            tmp = ListNode(head.val)
            if head.val < x:
                small.next = tmp
                small = small.next
            else:
                large.next = tmp
                large = large.next
        
            head = head.next
        
        small.next = largeHead.next
        
        return smallHead.next

'''
这是一个两根指针的题；需要新建一个节点分别代表头和尾
然后扫描整个链表，每次都新建一个节点，找到符合要求的
节点，分别接到当前节点上。

注意不需要单独处理node.val == x的情况
链表的问题要注意dummynode的使用
'''