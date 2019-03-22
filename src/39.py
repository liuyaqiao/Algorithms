class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []
        res = []
        self.dfs(candidates, target, [], res, 0)
        return res
        
    def dfs(self, candidates, target, temp, res, index):
        if target < 0:
            return
        if target == 0:
            res.append([] + temp)
        else:
            for i in range(index, len(candidates)):
                if i != 0 and candidates[i] == candidates[i - 1]:
                    continue
                temp.append(candidates[i])
                self.dfs(candidates, target - candidates[i], temp, res, i)
                temp.pop()

'''
这里是使用了减法的规则去遍历；

注意的有三处：
1. target - nums[i]要放在dfs中，不能放在递归之前；
2. 一定在return的时候要考虑全面，小于0的时候也要return
3. 考虑新的一次递归包不包括该数，用index还是index + 1
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not List:
            return []
        result = []
        self.helper([], candidates, 0, target, 0, result)
        return result
        
    def helper(self, temp, nums, tempSum, target, index, result):
        if tempSum == target:
            result.append([] + temp)
            return
        
        if tempSum > target:
            return
        
        for i in range(index, len(nums)):
            temp.append(nums[i])
            # tempSum += nums[i]
            self.helper(temp, nums, tempSum + nums[i], target, i, result)
            temp.pop()
        
'''
这个是加法规律；注意的点类似
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        result = []
        self.helper([], candidates, 0, target, 0, result)
        return result
        
    def helper(self, temp, nums, tempSum, target, index, result):
        if tempSum == target:
            result.append([] + temp)
            return
        
        if tempSum > target:
            return
        
        for i in range(index, len(nums)):
            temp.append(nums[i])
            tempSum += nums[i]
            self.helper(temp, nums, tempSum, target, i, result)
            val = temp.pop()
            tempSum -= val
        

'''
如果用tempSum写在调用外面，一定要记得回溯的时候减去这个值！

'''