# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    prev = None
    ## 这里需要储存一个lastNode，表示最后遍历的节点
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        
        self.prev = root
        


##divide and conquer

    def flatten(self, root):
        self.helper(root)
        
    # restructure and return last node in preorder
    def helper(self, root):
        if root is None:
            return None
            
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        # connect 
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
            
        if right_last is not None:
            return right_last
            
        if left_last is not None:
            return left_last
            
        return root


'''
一个树类型的题通常有两种方法：
1. tranverse : 用一个全局变量来记录tranverse的位置，注意一下遍历的顺序
2. divide and conquer: 两个递归的返回是一个实际的数值，一定要清楚它表示的意义，
这里就表示他的last_node，而且这个递归是有返回值的。所以原来函数没有返回就要新建一个
函数。
这里注意return值的确定，需要考虑是不是None的情况。

需要分别考虑left和right的返回，同时考虑集中情况。

'''