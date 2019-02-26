"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = collections.deque([root])
        result = []
        
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                temp = queue.popleft()
                if temp.children:
                    for item in temp.children:
                        queue.append(item)
                level.append(temp.val)
            result.append(level)
        return result