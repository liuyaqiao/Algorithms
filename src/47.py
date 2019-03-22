class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        res = []
        visited = [0 for i in range(len(nums))]
        nums.sort()
        self.dfs(res, [], nums, visited)
        return res
    
    def dfs(self, res, temp, nums, visited):
        if len(temp) == len(nums):
            res.append([] + temp)
        
        else:
            for i in range(len(nums)):
                if visited[i] == 1:
                    continue
                if i != 0 and nums[i] == nums[i - 1] and visited[i - 1] == 0:
                    continue
                    
                temp.append(nums[i])
                visited[i] = 1
                self.dfs(res, temp, nums, visited)
                visited[i] = 0
                temp.pop()


'''
排列与组合类似，有几个需要注意的地方：

1. 需要一个visited来跳过已经取过的数；
2. 数组一定要先排序
3. 去重：
    1）不是首元素
    2）和前一个元素相等
    3）前一个元素还没有取过
    (去一个)

'''