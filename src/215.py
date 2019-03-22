class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        k -= 1
        left = 0
        right = len(nums) - 1
        while True:
            p = self.partition(nums, left, right)
            if p == k:
                return nums[k]
            if p > k:
                right -= 1
            else:
                left += 1

    def partition(self, nums, left, right):
        p = left
        pivot = nums[right]
        for now in range(left, right):
            if nums[now] > pivot:
                nums[now], nums[p] = nums[p], nums[now]
                p += 1
        nums[p], nums[right] = nums[right], nums[p]
        return p