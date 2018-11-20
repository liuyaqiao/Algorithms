"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        
        result = []
        self.dfs(root, result)
        return result
    
    def dfs(self, root, result):
        if root == None:
            return
        for item in root.children:
            self.dfs(item, result)
        result.append(root.val)
        