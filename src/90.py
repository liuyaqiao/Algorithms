class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 0:
            return []
        
        nums.sort()
        visited = [0 for i in range(len(nums))]
        
        self.dfs([], res, 0, nums, visited)
        return res
    
    def dfs(self, temp, res, index, nums, visited):
        res.append(temp + [])
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            
            temp.append(nums[i])
            visited[i] = 1
            self.dfs(temp, res, i + 1, nums, visited)
            visited[i] = 0
            temp.pop()
            