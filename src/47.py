class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        res = []
        visited = [0 for i in range(len(nums))]
        nums.sort()
        self.dfs(res, [], nums, visited)
        return res
    
    def dfs(self, res, temp, nums, visited):
        if len(temp) == len(nums):
            res.append([] + temp)
        
        else:
            for i in range(len(nums)):
                if visited[i] == 1:
                    continue
                if i != 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
                    continue
                    
                temp.append(nums[i])
                visited[i] = 1
                self.dfs(res, temp, nums, visited)
                visited[i] = 0
                temp.pop()