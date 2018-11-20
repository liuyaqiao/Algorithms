"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        if root == None:
            return []
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, root, result):
        if root == None:
            return
        
        result.append(root.val)
        for item in root.children:
            self.helper(item, result)
    
        