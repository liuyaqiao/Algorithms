class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        
        
        ## map
        Hashmap = {}
        for pair in flights:
            if pair[0] in Hashmap:
                Hashmap[pair[0]] += [pair[1:3]]
            else:
                Hashmap[pair[0]] = [pair[1:3]]
        
        queue = collections.deque([(src, 0)])
        
        steps = 0
        res = []
        ans = float('inf')

        
        while queue:
            # steps += 1
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                cur = temp[0]
                cost = temp[1]

                if cur == dst:
                    ans = min(ans, cost)
                if cur not in Hashmap:
                    continue
                for nextCityList in Hashmap[cur]:
                    nextCity = nextCityList[0]
                    nextCost = nextCityList[1]
                    if nextCost + cost > ans:
                        continue
                    queue.append((nextCity, cost + nextCost))
                    
            steps += 1
            if steps > K + 1:
                break
                    
                    
        if ans == float('inf'):
            return -1
        return ans
'''
又是一个通过bfs来搜索最短路径的题目：
这道题与之前不同的地方在于，这个路径不是单纯的路径，而且带有权值，我们
要求的是权值最小。

1. 这时候我们的queue可以去存一个pair，出队的时候使用两个元素
queue中一个存的元素是第一个是[city, cost]
cost是当前最少的cost

2. 这里还用到的是一个pruning操作，当前的cost小于算出来的cost时，直接continue

3. 还要注意的是python中最大值和最小值的运用，float('inf') 和 -float('inf')

4. 当前元素不在hashmap时，这里应该用continue。

5. 结束的条件应该注意一下。

'''