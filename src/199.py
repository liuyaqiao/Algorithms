# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        
        queue = collections.deque([root])
        res = []
        while queue:
            
            for i in range(len(queue) - 1, -1, -1):
                temp = queue.popleft()
                if i ==  0:
                    res.append(temp.val)
                if temp.left != None:
                    queue.append(temp.left)
                if temp.right != None:
                    queue.append(temp.right)
        
        return res

'''
类似层次遍历：唯一不同的是只需要输出这一层的最后一个
我们需要把这个和循环的i建立联系，这里不能用len(queue)
来建立联系，因为queue长度会变，所有用了减小的循环。

'''