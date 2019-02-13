'''
K-th Element of Two Sorted Arrays
Given two sorted arrays of size m and n respectively, you are tasked with finding the element that would be at the k’th position of the final sorted array

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
    c = []
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        if a[i] < b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    
    if i < len(a):
        c.append(a[i])
        i += 1
    if j < len(b):
        c.append(b[j])
        j += 1
    print(c)


def findkth(a,b,k):

    if not a:
        return b[k]
    if not b:
        return a[k]

    la, lb = len(a)//2, len(b)//2
    ma, mb = a[la], a[lb]

    if la + lb < k:
        #第k大的值在右边，下面判断要去掉哪一部分的值
        if ma > mb:
            #说明肯定不在b的前半部分中
            return findkth(a, b[lb:], k - ib)
        else:
            return findkth(a[:ia + 1], k - ia])
    else:
        if ma > mb:
            return findkth(a[:ia], b, k)
        else:
            return findkth(a. b[:ib], k)



if __name__ == '__main__':
    a = [2,3,6,7,9]
    b = [1,4,8,10]
    print(findkth(a,b,3))·