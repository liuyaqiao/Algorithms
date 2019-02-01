        i = len(a) - 1
        j = len(b) - 1
        reminder = 0
        res = []
        while i >= 0 or j >= 0:
            _sum = reminder
            if i >= 0:
                _sum += eval(a[i])
                i -= 1
            if j >= 0:
                _sum += eval(b[j])
                j -= 1
            res.append(_sum % 2)
            reminder = _sum // 2
            
        if reminder == 1:
            res.append(reminder)
        
        result = ''
        for i in range(len(res) - 1, -1, -1):
            result = result + str(res[i])
            
            
        return result

'''
这是一个要求实现二进制运算的问题
要注意的几个问题：

1. 从数末尾开始循环，直到没有数。这里要写一个while 的循环，在合并数组的时候也会用到。
2. eval()取字符串的值
3. % 和 /的应用
'''