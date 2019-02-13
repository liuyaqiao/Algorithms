# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':
        if not head:
            return None
        
        dummyNode = ListNode(-1)
        dummyNode.next = head
        prev = dummyNode
        cur = head
        for i in range(1,m):
            prev = prev.next
            cur = cur.next
        
        
        for i in range(n - m):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next  #temp.next = cur
            prev.next = temp
        return dummyNode.next


'''
这是一个反转链表的follow up：
核心的关键点是把反转操作转换成一步一步的反转；
是一个只针对两个节点的操作，然后通过一个循环
去完成整个操作；
eg:
1->2->3->4->5   m = 2, n = 4
1)
1->3->2->4->5
2)
1->4->3->2->5
每次prev保持不变，通过cur的不断后移，把当前的节点扔到最前面去。
这就是我们这个题的思路
在循环中写链表的操作时，有一个比较tricky的地方是：
代码中注释的部分， 不能写成：
temp.next = cur
因为cur会不断移动，而要写成temp.next = prev.next

'''
