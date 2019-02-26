# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    sumVal = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ## right first -> root -> left last
        if not root:
            return None
        res = 0
        self.tranverse(root)
        return root
        
    
    def tranverse(self, root):
        if root == None:
            return
        
        self.tranverse(root.right)
        
        self.sumVal += root.val
        root.val = self.sumVal
        
        self.tranverse(root.left)

'''
注意：
这里不能把maxVal当成一个函数参数传入，因为python中不存在引用
传递，所以函数中改变的参数值不会反映在recursive函数外；所以这
里最好使用一个类的属性变量去记录；用cpp的时候，我们可以使用引用
来作为形参；

这个题要注意的是：
这是一个BST，所以我们可以知道大小顺序；思路类似于定义一个prev记
录上一次操作的重点，一次次类推的思路；这里inorder traversal不
单单是先左孩子，也可以先右孩子；
'''