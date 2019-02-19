# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ## 递归的出口：去查找A,B
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        # 左子树中有没有p,q

        right = self.lowestCommonAncestor(root.right, p, q)
        # 右子树中有没有p,q

        # 如果在左边找到了一个节点并且在右边也找到一个节点
        if left != None and right != None:
            return root
        
        # 如果都在左边
        if left != None:
            return left
        # 如果都在右边
        if right != None:
            return right
        # 如果都没有
        return None

'''
二叉树寻找最低公共祖先：
用了divide and conquer的方法：

关键点在于寻找整个树的结果和根、左子树和右子树之间的关系：

这里的关系为：

root left right :

1. 如果p,q分别在left和right中，lca是root
2. 如果left = None, 那么LCA就是右边的LCA。
3. 如果right = None， 那么LCA就是左边的LCA。



'''