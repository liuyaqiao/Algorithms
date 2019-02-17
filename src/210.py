class Solution:
    def findOrder(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
#         if not prerequisites:
        if numCourses <= 0:
            return []
        
        ##hashmap
        HashMap = {}
        for pair in prerequisites:
            if pair[1] in HashMap:
                HashMap[pair[1]] += [pair[0]]
            else:
                HashMap[pair[1]] = [pair[0]]
        
        
        ##indegree
        indegree = [0 for _ in range(numCourses)]
        
        for pair in prerequisites:
            indegree[pair[0]] += 1
            
        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        res = []
        
        while queue:
            course = queue.popleft()
            if course not in HashMap:
                res.append(course)
                continue
            nextCourse = HashMap[course]
            
            for item in nextCourse:
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)
            res.append(course)
        
        # print (res)
            
        if len(res) == len(indegree):
            return res
        return []

'''
类似于拓扑排序的问题：
要求输出一个有可能的排序

思路还是bfs的思路，通过bfs来遍历整个图，唯一不同的是
在bfs之中需要加一个result去储存每一次queue pop的结果。
最后通过判断result的长度和课程数的大小来判断是否满足要求。

之前的indegree和hashmap的操作都操作和之前的习题类似


'''