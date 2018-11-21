# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    # 返回和为RemainTarget的 所有可能的节点 组成的集合
    # subset[[1,3], [2,2]] target = 4
    def FindPath(self, root, expectNumber):
        # write code here
         
        result = []
        if root == None:
            return result
        self.dfs(root, expectNumber, [], result)
        return result

    def dfs(self, root, remainNumber, path, result):
        ##加法
        if root == None:
            return
        path.append(root.val)
        if root.left == None and root.right == None and sum(path) == remainNumber:
            result.append([] + path)
        if root.left:
            self.dfs(root.left, remainNumber, path, result)
        if root.right:
            self.dfs(root.right, remainNumber, path, result)
        path.pop()
        
        

        #减法dfs
        
        
        
        ##
        '''

        分治法
        result = []

        if root == None:
            return []

        if root.left == None and root.right == None:
            if expectNumber == root.val:
                return [[root.val]]
            else:
                return []

        left = self.FindPath(root.left, expectNumber - root.val)
        for path in left:
            path.insert(0, root.val)
            result.append(path)
        right = self.FindPath(root.right, expectNumber - root.val)
        for path in right:
            path.insert(0, root.val)
            result.append(path)
        return result
        '''    
        