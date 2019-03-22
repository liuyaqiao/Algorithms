"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        queue = collections.deque([root])
        
        while queue:
            prev = None
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                
                if prev != None:
                    prev.next = temp
                    
                prev = temp
                    
        return root
                
'''
层次遍历：
加一个prev变量表示前一次遍历的节点；
给当前的prev初始值设为0，然后每次赋予它temp的值是一个很常见的方法

'''