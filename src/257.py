# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        if root == None:
            return []
        
        result = []
        
        self.dfs(root, '', result)

        return result
        
    def dfs(self, root, temp, result):
        if root.left == None and root.right == None:
            
            temp += str(root.val)
            result.append(temp + "")
            return
        else:
            # temp.append(root.val)
            if root.left != None:
                self.dfs(root.left, temp + str(root.val) + '->', result)
            if root.right != None:
                self.dfs(root.right, temp + str(root.val) + '->', result)