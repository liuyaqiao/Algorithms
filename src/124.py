# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = -float('inf')
    def maxPathSum(self, root: TreeNode) -> int:
        ##postorder
        if not root:
            return 0
        self.tranverse(root)
        return self.res

    def tranverse(self, root):
        #res max positive sum
        if root == None:
            return 0
        
        left = max(0, self.tranverse(root.left))
        right = max(0, self.tranverse(root.right))
        
        self.res = max(self.res, left + right + root.val)
        
        return max(left, right) + root.val
    
'''
1. 遇到与树相关的问题，首先要判断这个用那种遍历法比较合适：
inorder, preorder, postorder. 这决定了代码迭代的顺序。
这个题就是使用postorder，所以先进行递归调用；然后在去处理
根节点；

2. 在这里要考虑负数的情况，有负数的情况要用max(0, )的形式
把负数的情况去掉。

3. res = root.val + left + right

4. 确定helper函数的返回值，明确它的意思；写返回值；
'''