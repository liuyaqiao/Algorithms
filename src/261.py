class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        hashmap = {i : [] for i in range(n)}
        
        for a,b in edges:
            hashmap[a].append(b)
            hashmap[b].append(a)
            
        
        queue = collections.deque([0])
        visited = [False for _ in range(n)]
        result = []
        
        while queue:
            temp = queue.popleft()
            visited[temp] = True
            result.append(temp)
            for item in hashmap[temp]:
                if visited[item] == False:
                    visited[item] = True
                    queue.append(item)
        print(result)
        return len(result) == n
    
    
'''
bfs:
注意的点：
1. 先判断点edge的个数和点的数目，这是一个最直接的标准
2. 用bfs走一遍，用一个set或者list储存走过的点，如果全走过就是true，没有就是false
3. 这种edge中没有出现所有节点的情况，可以使用这种方法来建立字典
4. 这种无向图要左右都连起来
'''