class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        
        visited = [0 for _ in range(len(M))]
        hashmap = collections.defaultdict(list)
        for row in range(len(M)):
            for col in range(row):
                if M[row][col] == 1:
                    hashmap[row].append(col)
                    hashmap[col].append(row)
        count = 0              
        for i in range(len(M)):
            if visited[i] == 1:
                continue
            count += 1
            queue = collections.deque([i])
            visited[i] = 1
            
            while queue:
                temp = queue.popleft()
                for j in hashmap[temp]:
                    if visited[j] == 0:
                        queue.append(j)
                        visited[j] = 1
                        
        return count
                
'''
bfs 需要注意的地方:
1. 建立hashmap的时候需要建立双向hash，同时最好还是用defaultdict
2. 通过矩阵建立的时候可以以row，col为解，不访问对角线
3. count来计数
‘’‘