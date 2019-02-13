# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root, -float("inf"), float("inf"))
        
    def helper(self, root, minValue, maxValue):
        if root == None:
            return True
        if root.val >= maxValue or root.val <= minValue:
            return False
        return self.helper(root.left, minValue, root.val) and self.helper(root.right, root.val, maxValue)
        

        
'''
这个题是树形dfs的，我们使用递归来解决：

这里的关键点在于我们如何定义递归返回的条件

这里我们不能简单的判断当前节点和它的left、right的大小
来判断，因为下面的left的right可能会大于parent节点，这
是这个条件不能判断的。

所以，我们需要设定一个当前最大值和最小值。当前的最大值和最小值
由当前的节点所决定，而初始的状态是由inf来决定。

这里要留意一下，最大值和最小值的方式：

max = float("inf")
min = -float("inf")

'''