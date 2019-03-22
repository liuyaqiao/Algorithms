class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum2(self, candidates, target):
        # write your code here
        results = []
        if candidates == None:
            return results
        candidates.sort()
        self.dfs(candidates, 0, target, [], results)
        return results
    #递归的定义
    #找到所有以combanation 开头 和为target的组合 并放入result， 其中剩余需要加入combanation数的和为remainTarget
    #并且下一个加入的位置从startindex开始
    def dfs(self, candidates, startIndex, remainTarget, combination, results):
        if remainTarget < 0:
            return

        if remainTarget == 0:
            results.append([] + combination)
        else:
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                self.dfs(candidates,i + 1,remainTarget - candidates[i], combination, results)
                combination.pop()

            

