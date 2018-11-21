# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        import Queue
        result = []
        q = Queue.Queue()
        if root == None:
            return result
        q.put(root)
        while q.qsize() != 0:
            for i in range(q.qsize()):
                temp = q.get()
                result.append(temp.val)
                if temp.left != None:
                    q.put(temp.left)
                if temp.right != None:
                    q.put(temp.right)
        return result
                