# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        newHead = head
        while head:
            temp = head.next
            if temp == None:
                newHead = head       
            head.next = prev
            prev = head
            head = temp
        return newHead        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
            
        return prev

'''
链表反转：

主要分四部：

1. 建立temp节点来表示当前的头节点
2. 头节点移位
3. temp节点和prev节点连接
4. 更新prev节点

注意的是，return的时候要返回的是prev节点。


'''