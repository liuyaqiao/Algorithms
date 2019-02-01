# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        #corner case
        if head == None or head.next == None:
            return head

        
        headNode = ListNode(-1)
        headNode.next = head
        length = 1        
        while head.next != None:
            head = head.next
            length += 1
        head.next = headNode.next
        
        head = headNode.next
        for i in range(1, length - k % length):
            head = head.next
        
        newHead = head.next
        head.next = None

        
        return newHead


'''
这是一个linkedlist的题目，具体代码比较简单主要是思路：

1. 将链表首尾相连这是一个针对链表旋转操作的好方法
2. 针对循环超过length的问题，要记住对length取余数的操作
3. 对链表长度等这种从1开始的量，要在循环i的取值的时候注意一下

'''