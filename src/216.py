class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = [1,2,3,4,5,6,7,8,9]
        self.dfs([], res, 0, k, n, candidates)
        return res
    
    
    def dfs(self, temp, res, startIndex, k, target, candidates):
        if len(temp) > k or target < 0:
            return
        if len(temp) == k and target == 0:
            res.append([] + temp)
        else:
            for i in range(startIndex, len(candidates)):
                temp.append(candidates[i])
                # print(temp)
                self.dfs(temp, res, i + 1, k, target - candidates[i], candidates)
                temp.pop()