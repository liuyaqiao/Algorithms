# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    first = None
    second = None
    prev = None
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.dfs(root)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp
        
    def dfs(self, root):
        if root == None:
            return
        self.dfs(root.left)
        if self.prev != None and self.prev.val >= root.val:
            if self.first == None:
                self.first = self.prev
            
            self.second = root
        self.prev = root
        self.dfs(root.right)

        
'''
首先要确定是一个先序遍历解决的题
所以按照先序遍历的写法开始写：
找到两个不满足中序遍历的点记录，然后交换他们的值
这里要有一个prev指针去储存当前遍历的位置；
一个比较tricky的地方是：
这里的second = root，因为first已经被赋值
这里second不能在赋成prev

'''