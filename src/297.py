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
            return ""
        
        queue = collections.deque([root])
        res = []
        
        while queue:
            node = queue.popleft()
            res.append(str(node.val) if node else 'null')
            if node:
                # res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
                
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        bfs_order = [
            TreeNode(int(val)) if val != 'null' else None
            for val in data.split()
        ]

        root = bfs_order[0]
        fast_index = 1
        
        nodes, slow_index = [root], 0
        while slow_index < len(nodes):
            node = nodes[slow_index]
            slow_index += 1
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            fast_index += 2
            
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

'''
树的序列化和反序列化，序列化用bfs做。
反序列化是就是按照这个数组挨个复原。
尽量避免递归的调用，这个数组和heap的存储结构类似。
可以用一个slow一个fast挨个遍历。

通过一个split来断开每一个字符

'''