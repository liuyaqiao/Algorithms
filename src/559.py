"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    depth = 0
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root, 1)
        return self.depth
        
    def helper(self, root, res):
        if root == None:
            return
        self.depth = max(self.depth, res)
        for item in root.children:
            self.helper(item, res + 1)

        
        
        
        
        