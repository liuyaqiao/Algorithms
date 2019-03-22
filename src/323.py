class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n < 0 :
            return 0
        if not edges:
            return n
        
        hashmap = {}
        for edge in edges:
            if edge[0] in hashmap:
                hashmap[edge[0]].append(edge[1])
            else:
                hashmap[edge[0]] = [edge[1]]
        
        for edge in edges:
            if edge[1] in hashmap:
                hashmap[edge[1]].append(edge[0])
            else:
                hashmap[edge[1]] = [edge[0]]
            
        visited = [0 for _ in range(n)]
        queue = collections.deque([])
        count = 0

        for i in range(n):
            if visited[i] == 1:
                continue
            queue.append(i)
            visited[i] = 1
            while queue:
                temp = queue.popleft()
                if temp not in hashmap:
                    continue
                for item in hashmap[temp]:
                    if visited[item] != 1:
                        queue.append(item)
                        visited[item] = 1        
            count += 1
            
        return count
                
'''
无向图有关的哈希表建立要建立一个双向的hash，不能按照给出
的list建立单项hash。

关于建立hashmap有一个优化：

    adj = collections.defaultdict(list)
    for (u, v) in edges:
        adj[u].append(v)
        adj[v].append(u)

'''