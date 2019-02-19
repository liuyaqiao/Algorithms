"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    prev = None
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        # self.prev = None
        dummyNode = Node(-1, None, None)
        self.prev = dummyNode
        
        self.tranverse(root)
        ## right表示next, left表示prev
        
    
        ## 最后的指针建立
        self.prev.right = dummyNode.right
        dummyNode.right.left = self.prev
        
        ##
        return dummyNode.right
    
    def tranverse(self, root):
        if root == None:
            return
        
        self.tranverse(root.left)
        
        self.prev.right = root
        root.left = self.prev
        self.prev = root
        
        self.tranverse(root.right)
        
        

'''
把二叉树改写成双向链表：

1.思路是用tranverse的方法挨个实现；这里我们要用到一个全局的prev指针
2.这里全局prev，这里成为类的成员变量的声明有三种方式：
    1. 通过__init__(self):
    2. 直接在class下面：prev = None
    3. 在函数里面 self.prev = None
3.在做完prev和root的操作之后，要记得操作头和尾；
链表改变的操作需要使用dummyNode

'''