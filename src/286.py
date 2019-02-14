class Solution:
    def wallsAndGates(self, rooms: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        if not rooms:
            return
        
        rows = len(rooms)
        cols = len(rooms[0])
        
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue = collections.deque([])
                    queue.append((i + 1, j, 1))
                    queue.append((i - 1, j, 1))
                    queue.append((i, j + 1, 1))
                    queue.append((i, j - 1, 1))
                    visited = set()
                    
                    while queue:
                        x, y, val = queue.popleft()
                        if x < 0 or x >= rows or y < 0 or y >= cols or rooms[x][y] in [0, -1] or (x, y) in visited:
                            continue
                        visited.add((x, y))
                        rooms[x][y] = min(rooms[x][y], val)
                        
                        queue.append((x + 1, y, val + 1))
                        queue.append((x - 1, y, val + 1))
                        queue.append((x, y - 1, val + 1))
                        queue.append((x, y + 1, val + 1))
                    
                    
        
'''
和number of islans 类似，一道典型的bfs
bfs有几个关键点：
1. queue python中要使用collections.deque去创建，这里出队的时间复杂度是O（1）
2. 需要一个visited数组，去记录当前该点是否被读取
3. 需要判断当前的取出的点是否会越界

'''