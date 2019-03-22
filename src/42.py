class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]
        
        for i in range(len(height)):
            if i != 0:
                left[i] = max(left[i - 1], height[i - 1])
        for i in range(len(height) - 1, -1 , -1):
            if i != len(height) - 1:
                right[i] = max(right[i + 1], height[i + 1])
        
        
        res = [0 for _ in range(len(height))]
        
        for i in range(len(height)):
            res[i] = max(min(left[i], right[i]) - height[i], 0)
        
        return sum(res)


    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        leftmost = 0
        rightmost = 0
        res = 0
        
        while left < right:
            leftmost = max(height[left], leftmost)
            rightmost = max(height[right], rightmost)
            
            if leftmost < rightmost:
                res += (leftmost - height[left])
                left += 1
            else:
                res += (rightmost - height[right])
                right -= 1
                
        return res

'''
两个two pointer的方法：

1.需要用一个extra space去储存当前左边的最大值和当前右边的最大值，
可以储存的雨水就等于left和right的最小值在加上当前的高度

2.用一个leftmost和一个rightmost的变量去储存当前所经过的最大值。
总体来说是一个累计的方法；每次遍历到一个位置都去填平当前位置和left，
right中较小的值。所填充的值就是储存的水。

'''