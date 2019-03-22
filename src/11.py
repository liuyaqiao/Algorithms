class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(area, res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return res