class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        
        res = []
        # res.append([])
        self.dfs([], res, nums, 0)
        # print(res)
        return res
        
    def dfs(self, temp, res, nums, index):
        res.append(temp + [])
        
        for i in range(index, len(nums)):
            # print(i)
            temp.append(nums[i])
            # print(temp)
            self.dfs(temp, res, nums, i + 1)
            temp.pop()
            
        
        