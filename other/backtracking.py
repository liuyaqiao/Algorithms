def findThree(nums):
    state = [True for _ in range(len(nums))]
    result = []
    dfs(nums, [], 0, result)

    return result

def dfs(nums, temp, index, result):
    if len(temp) == 3:
        result.append([] + temp)
        return
    
    for i in range(index, len(nums)):
        temp.append(nums[i])
        dfs(nums, temp, i + 1, result)
        temp.pop()



if __name__ == '__main__':
    nums = [1,2,3,4,5]
    print (findThree(nums))


'''
这里来说一下backtracking的一个整体框架和思路：
整个backtracking有四个关键点：
1. 我们要用dfs
2. 在递归中要记得设定end point
3. 对合理的结果要记得保存
4. 为了节省复杂度，要使用pruning的操作


有一个代码框架：

if (solution is well) :
    add solution
    return

for x :   dfs
    if condition:
        solution
        dfs
        pop


'''