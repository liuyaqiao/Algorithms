class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        result = []
        self.dfs(nums, [], result, 0)
        return result
        
        
    def dfs(self, nums, temp, result, index):
        result.append(temp + [])
        
        for i in range(index, len(nums)):
            if i > index and nums[i - 1] == nums[i]:
                continue

            temp.append(nums[i])
            self.dfs(nums, temp, result, i + 1)
            temp.pop()

'''
1. 判断和前面的数字相等
'''