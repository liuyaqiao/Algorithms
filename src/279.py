class Solution(object):
    # import math
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            exit
        queue = collections.deque([n])
        depth = 0
        while queue:
            depth += 1
            size = len(queue)
            for i in range(size):
                curt = queue.popleft()
                for j in range(1, curt):
                    if j * j > curt:
                        break
                    res = curt - j * j
                    
                    if res == 0:
                        return depth
                    else:
                        queue.append(res)
        return depth


'''

这是一个可以用bfs、dfs和dp解决的问题：
用bfs时的关键在于写出搜索树；通过搜索数去寻找当前层和下一层
之间的关系；

这种需要搜索去找最小值的问题通常会用到bfs。因为bfs是按照层进行搜索
他可以搜索在最短的层数。

这里有一个值得注意的地方，是关于平方数和开方数，为了避免不精确，我们一般
不使用sqrt，而用i*i > j的格式去表示。

'''