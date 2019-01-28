# Summary

## 双指针问题心得

几个关键的点：

1. 能使用双指针的条件是一次指针的变动可以去掉一类解，所以这就要求我们先对数组进行排序；
2. 这里需要掌握一个去重的技巧：
```
while left < right and nums[left] == nums[left - 1]:
    left += 1
while left < right and nums[right] == nums[right + 1]:
    right -= 1

for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    这里使用时需要注意，i > 0这个条件要在前面防止越界。
```

