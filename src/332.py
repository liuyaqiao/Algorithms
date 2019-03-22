class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return None
        targets = collections.defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            targets[a].append(b)
        route = []
        self.dfs(targets, route, "JFK")
        return route[::-1]
        
    def dfs(self, targets, route, start):        
        while targets[start]:
            self.dfs(targets, route, targets[start].pop())
        route.append(start)
            
'''
1. collections.default(list)的运用：这里判断没有元素不用用if s[i]的形式，必须是s[i] != None
2. 在dfs中有一个循环，是要遍历hash对集合中对应的所有元素,这个搜索类似与tree的先序后序遍历一样，搜索
到头在回溯的过程中进行append。而不能使用for的方式去同时遍历一个hash中的所有值。
 

'''