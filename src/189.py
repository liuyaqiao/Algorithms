class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # if k > len(nums):
        #     return
        k = k % len(nums)
        a = len(nums)
        nums.reverse()
        nums1 = nums[0:k]
        nums2 = nums[k:len(nums)]
        nums1.reverse()
        nums2.reverse()
        for i in range(0, k):
            nums[i] = nums1[i]
        for i in range(k, a):
            nums[i] = nums2[i-k]

