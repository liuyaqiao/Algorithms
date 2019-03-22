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
        
        if root.left:
            root.left.next = root.right
        
        if root.right and root.next:
            root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
        
        return root

'''
1. root节点初始化的next值就是None，所以不需要管
2. 凡事这种需要通过根节点来操作left和right节点的题目一般都是preorder
3. 注意一下啊root.right and root.next的判断条件；

'''