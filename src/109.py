# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    current = None
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        self.current = head
        size = self.getSize(head)
        
        return self.Build(size)
        
    def Build(self, size):
        if size <= 0:
            return None
        
        left = self.Build(size//2)
        root = TreeNode(self.current.val)
        self.current = self.current.next
        right = self.Build(size - 1 - size//2)
        
        root.left = left
        root.right = right
        
        return root
                
        
    def getSize(self, head):
        size = 0
        while head != None:
            size += 1
            head = head.next
        return size


'''
采用分治的方法去解决，需要注意的点如下：

1. 首先要把链表截断，写一个getsize的函数
2. 和数组不同，可以进行直接划分，这里需要用一个current指针
记录当前head的位置。

'''