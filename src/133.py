# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        root = node
        if not node:
            return None
        
        ## to have a nodes list
        queue = collections.deque([node])
        nodes = set([node])
        
        while queue:
            head = queue.popleft()
            for neighbor in head.neighbors:
                if neighbor not in nodes:
                    nodes.add(neighbor)
                    queue.append(neighbor)
                    
        ## old to new map & deep copy node
        Hashmap = {}
        for node in nodes:
            Hashmap[node] = UndirectedGraphNode(node.label)
        
        ## deep copy neighbor
        
        for node in nodes:
            new_node = Hashmap[node]
            for neighbor in node.neighbors:
                new_neighbor = Hashmap[neighbor]
                new_node.neighbors.append(new_neighbor)
                
        return Hashmap[root]


'''
bfs

tricky:
1. 建立old_node 和 new_node之间的mapping
2. 首先要取得node的一个集合，这个在bfs中比较常见：通过一个循环，来获得当前图node和neighbor的对应关系；
这里是获得了old和new的对应关系。取这个集合的时候用到了bfs.
3. 在构建新的节点时，按照顺序来，首先新建node，在有了node的基础上去新建neighors。

'''

        