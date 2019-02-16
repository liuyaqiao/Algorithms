class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        if not prerequisites:
            return True
        
        indegree = [0 for _ in range(numCourses)]
        for pair in prerequisites:
            indegree[pair[0]] += 1
        HashMap = {}
        for pair in prerequisites:
            if pair[1] in HashMap.keys():
                HashMap[pair[1]] = HashMap[pair[1]] + [pair[0]]
            else:
                HashMap[pair[1]] = [pair[0]]
                
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            if course not in HashMap:
                continue
            nextCourse = HashMap[course]

            for item in nextCourse:
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)

        
        for i in range(numCourses):
            if indegree[i] != 0:
                return False
        return True

'''
一个bfs的题，解体过程可以分成一下几步：

1. 建立一个map，先修和后修的map，这里要注意一下当前元素是否存在于dict中的写法
2. 建立一个indegree table，每次有先修课修完indegree - 1
3. bfs的queue

'''