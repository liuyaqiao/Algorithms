# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        result = []
        self.traverse(root, result)
        
        return ' '.join(result)
    
    def traverse(self, root, result):
        if not root:
            return
        
        result.append(str(root.val))
        self.traverse(root.left, result)
        self.traverse(root.right, result)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        data = data.split()
        queue = collections.deque([])
        for s in data:
            queue.append(int(s))
        
        return self.helper(queue)
        
        
    def helper(self,queue): 
        if not queue:
            return None
        
        root = TreeNode(queue.popleft())
        smallQueue = collections.deque([])
        while queue and queue[0] < root.val:
            smallQueue.append(queue.popleft())
        root.left = self.helper(smallQueue)
        root.right = self.helper(queue)
        return root
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))