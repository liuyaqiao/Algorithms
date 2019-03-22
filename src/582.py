class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        if not pid or not ppid:
            return []
        if kill not in pid:
            return pid
        
        ## create a hashmap
        hashmap = {}
        for i in range(len(ppid)):
            if ppid[i] not in hashmap:
                hashmap[ppid[i]] = [pid[i]]
            else:
                hashmap[ppid[i]].append(pid[i])
        
        result = []
        queue = collections.deque([kill])
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                if temp in hashmap:
                    queue.extend(hashmap[temp])
                result.append(temp)
            
        return result