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

## python class 变量声明：

在python类的定义中，基本有三种方式：

```
1.
class A():
    def __init__(self):
        self.nums = []
    def update(self):
        self.nums.append(1)
        print (self.nums)
        
print:
[1]
[1]
[1]

2.
class A():
    nums = []
    def update(self):
        self.nums.append(1)
        print (self.nums)

print:
[1]
[1,1]
[1,1,1]

3.
class A():
    def update(self):
        self.nums = []
        self.nums.append(1)
        print (self.nums)
        
print:
[1]
[1]
[1]


test:

if __name__ == "__main__":
    a = A()
    a.update()
    b = A()
    b.update()
    c = A()
    c.update()
```

在第二种写法，我们这里的nums被所有的对象所共有；一个对象的改变就会带来所有对象中nums的改变。
