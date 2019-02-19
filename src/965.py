# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        left = self.isUnivalTree(root.left)
        right = self.isUnivalTree(root.right)
        
        if root.left != None and root.left.val != root.val:
            return False
        
        if root.right != None and root.right.val != root.val:
            return False
        
        return left and right
## 另一种比较巧妙的divide and conquer
    def isUnivalTree(self, root)
        if not root:
            return True
        self.val = root.val
        return self.tranverse(root)
        
        
    def tranverse(self, root):
        if root == None:
            return True
            
        if root.val != self.val:
            return False
            
        return self.tranverse(root.left) and self.tranverse(root.right)

## tranverse
    def isUnivalTree(self, root)
        self.Is = True
        if not root:
            return True
        self.val = root.val
        self.tranverse(root)
        return self.Is
        
        
    def tranverse(self, root):
        if root == None:
            return
            
        if root.val != self.val:
            self.Is = False
            
        self.tranverse(root.left) 
        self.tranverse(root.right)


'''
tranverse 的 helper函数一般只有遍历的功能，它的返回值是None。所以我们一般需要一个
全局变量去改变树的状态。

divide and conquer则是把当前函数的输出传给下一层递归函数。这里的参数一般来说和原题
中要求的一样，如果需要新加入入口参数，则需要改写函数入口。

'''
        
        