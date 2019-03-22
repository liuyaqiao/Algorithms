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


##divide and conquer

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        if root.left == None and root.right == None:
            return [str(root.val)]
        
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        
        paths = []
        
        for path in left:
            paths.append(str(root.val) + '->' + path)
            
        for path in right:
            paths.append(str(root.val) + '->' + path)
            
        return paths
            
    


    ##tranverse

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
        if not root:
            return []
        result = []
        self.dfs(root, result, [str(root.val)])
        return result
        
    def dfs(self, root, result, path):
        if root.left == None and root.right == None:
            result.append('->'.join(path))
            return
        
        if root.left:
            path.append(str(root.left.val))
            self.dfs(root.left, result, path)
            path.pop()
            
        if root.right:
            path.append(str(root.right.val))
            self.dfs(root.right, result, path)
            path.pop()


'''
总体思路类似：但是其实的条件需要注意
这里root要首先放入到result中

这里要放入下一个节点，不能放入当前节点；因为当前节点的话，根会被操作两次；

'''

