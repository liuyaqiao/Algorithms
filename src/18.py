class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if len(nums) < 4:
            return []
        
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target1st = target - nums[i]
            for j in range(i + 1, len(nums)):
                #去重#
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                target2nd = target1st - nums[j]
                left = j + 1
                right = len(nums) - 1
                
                while left < right:
                    if nums[left] + nums[right] == target2nd:
                        temp = []
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[left])
                        temp.append(nums[right])
                        res.append(temp)
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] < target2nd:
                        left += 1
                    else:
                        right -= 1
        return res
                
                
'''
这是two pointers的follow up题型，有几点需要注意的地方：
1. 思路：
整体的思路是这样的：把一个数组排序之后使用两根指针分别从头和尾部开始扫描，根据和目标值的大小可以直接去掉一种情况。
如果是3 sum的情况，则我们需要两重循环：第一重对target可能的取值进行扫描，第二层在进行two sum的操作。这里
two sum开始的位置一定是扫描的下一个位置。
4 sum 也是在这个基础上，使用了三重循环：每一重循环都从前面取值的下一个开始，最内层循环做一个two sum的操作。

2.注意事项：
这里的一个去重操作是我们很多情况都会碰到的：
    if i > 0 and nums[i] == nums[i - 1]:
        continue
i > 0这段代码要写在前面；

第二段去重写在if里面，所以可以写成
nums[right] == nums[right + 1]:
不会发生越界的现象

'''