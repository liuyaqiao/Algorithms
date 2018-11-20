# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            temp = 0
            l = len(stack)
            for i in range(len(stack)):
                t = stack.pop(0)
                ##pop操作时返回最后一个元素
                temp += t.val
                if t.left != None:
                    stack.append(t.left)
                if t.right != None:
                    stack.append(t.right)
            result.append(float(temp/l))
        
        return result