# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        while queue:
            length = len(queue)
            tempSum = 0
            for i in range(length):
                temp = queue.popleft()
                tempSum += temp.val
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                    
            res.append(tempSum * 1.0/length)
        
        
                
        return res