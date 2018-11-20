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