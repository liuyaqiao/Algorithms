class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return []
        nums = [i + 1 for i in range(n)]
        result = []
        self.helper(nums, [], result, 0, k)
        return result
    
    def helper(self, nums, temp, result, index, k):
        if len(temp) == k:
            result.append([] + temp)
            
        for i in range(index, len(nums)):
            temp.append(nums[i])
            self.helper(nums, temp, result, 1 + i, k)
            temp.pop()