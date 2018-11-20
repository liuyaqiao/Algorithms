class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        
        nums = [i for i in range(1, n + 1)]
        result = []
        self.dfs(nums, result, 0, [], k)
        
        return result
        
        
    def dfs(self, nums, result, index, temp, k):
        if len(temp) == k:
            result.append(temp + [])
        else:
            for i in range(index, len(nums)):
                temp.append(nums[i])
                self.dfs(nums, result, i + 1, temp, k)
                temp.pop()
    