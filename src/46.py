class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        
        res = []
        visited = [0 for i in range(len(nums))]
        # numSet = set()
        # self.dfs(nums, numSet, [], res)
        self.dfs(nums, visited, [], res)
        return res
    
    def dfs(self, nums, visited, temp, res):
        if len(temp) == len(nums):
            res.append([] + temp)
        else:
            for i in range(len(nums)):
                # if nums[i] in numSet:
                #     continue
                if visited[i] == 1:
                    continue
                    
                temp.append(nums[i])
                # numSet.add(nums[i])
                visited[i] = 1
                self.dfs(nums, visited, temp, res)
                # numSet.remove(nums[i])
                visited[i] = 0
                temp.pop()
        