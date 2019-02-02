# -*- coding: utf-8 -*-
'''
K-th Element of Two Sorted Arrays
Given two sorted arrays of size m and n respectively, you are tasked with finding 
the element that would be at the k’th position of the final sorted array
Input : Array 1 - 2 3 6 7 9
        Array 2 - 1 4 8 10
        k = 5
Output : 6
Explanation: The final sorted array would be -
1, 2, 3, 4, 6, 7, 8, 9, 10
The 5th element of this array is 6.
Input : Array 1 - 100 112 256 349 770
        Array 2 - 72 86 113 119 265 445 892
        k = 7
Output : 256
Explanation: Final sorted array is -
72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892
7th element of this array is 256.
'''


def kthLargest(a,b,k):
    # brute force
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    print(i, j)
    if i < len(a):
        while i < len(a):
            c.append(a[i])
            i += 1
    if j < len(b):
        while j < len(b):
            c.append(b[j])
            j += 1
    
    return c[k - 1]


def findKth(a,b,k):
    #找的是第k小的
    #使得a数组比b数组短：
    if len(a) > len(b):
        a, b = b, a
    if not a:
        #这里k表示第几个，所以和index的关系是index - 1
        return b[k - 1]
    if k == 1:
        #找的是第k小的，所以要返回一个min
        return min(a[0], b[0])
    
    pa = min(k//2, len(a))
    pb = k - pa

    if a[pa - 1] <= b[pb - 1]:
        return findKth(a[pa:], b, k - pa)
    else:
        return findKth(a, b[pb:], k - pb)
    
if __name__ == '__main__':
    a = [1,2,13,14,15]
    b = [6,7,8,9,17,18]
    for i in range(1, len(a) + len(b)):
        print(findKth(a,b,i))