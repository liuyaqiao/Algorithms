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


'''
回溯法：

注意的几个地方：

1. result.append() 必须要新建一个string或者list，需要用[] + / '' +
2. 传入参数的时候temp要更新，这里直接在参数中更新了，如果不是，需要在调用函数之后返回
   之前的样子。

'''