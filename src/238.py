class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        
        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]
        
        for i in range(len(left)):
            if i != 0:
                left[i] = nums[i - 1] * left[i - 1]
                
        for i in range(len(right) - 1, -1, -1):
            if i != len(right) - 1:
                right[i] = nums[i + 1] * right[i + 1]
        
        res = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
            
        return res

'''
很重要的一个思路：

1. 一个小型的dp思路；通过一个循环求出当前左边和右边的乘积；
再通过一个循环求出所求的res，这里是一个根据上一个状态求当前
状态的dp问题。
2. 可以通过一个变量来代替整体数组；达到这样的效果，可以减少
空间复杂度
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        lpd = rpd = 1
        nums_len = len(nums)
        for i in range(nums_len):
            res[i] = lpd
            lpd *= nums[i]

        for i in range(nums_len - 1, -1, -1):
            res[i] *= rpd
            rpd *= nums[i]

        return res