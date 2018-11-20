class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        if nums[start] > target:
            return start
        if nums[end] < target:
            return end + 1
        return start + 1
