class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        maxStep = 0
        for i in range(len(nums)):
            if i > maxStep:
                return False
            
            maxStep = max(nums[i] + i, maxStep)
        return True

'''
题目为给定一个数组，求能不能走到终点：

这是一个可以用贪心策略来解决的；贪心的意思就是当前最好的情况；

这种简单的问题一定要注意把数组和index结合起来去思考；

我们用一个变量来存放当前可以走到的最远值，只要这个最大值小于
当前的位置，我们就说失败了；最大值的更新由当前可以走的最大步
数加当前坐标更新决定；我们遍历整个数组就可以得到最大值；
'''