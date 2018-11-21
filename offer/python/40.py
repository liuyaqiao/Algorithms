import random
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k == 0:
            return []
        left = 0
        right = len(tinput) - 1
        p = self.Parition(tinput, 0, len(tinput) - 1)
        while p + 1 != k:
            if p + 1 > k:
                right = p - 1
            else:
                left = p + 1
            p = self.Parition(tinput, left, right)
        result = tinput[0:p+1]
#        result.sort()
        return result

    def Parition(self, tinput, left, right):
        # return position p(left less the tinput[p], right larger than tinput[p])
        rand = random.randint(left, right)
        tinput[right], tinput[rand] = tinput[rand], tinput[right]
        p = left
        pivot = tinput[right]
        for now in range(left, right):
            if tinput[now] < pivot:
                tinput[now], tinput[p] = tinput[p], tinput[now]
                p += 1
        tinput[p], tinput[right] = tinput[right], tinput[p]
        return p
        
####heap
        def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput) or k == 0:
            return []
        Heap = tinput[:k]
        for i in range(len(Heap) - 1, -1, -1):
            self.MaxHeapify(Heap, i, len(Heap))
        # print(Heap)
        for i in range(k, len(tinput)):
            if Heap[0] <= tinput[i]:
                continue
            else:
                Heap[0] = tinput[i]
                self.MaxHeapify(Heap, 0, len(Heap))
        Heap.sort()
        return Heap
    def MaxHeapify(self, A, i, size):
        l = 2 * i + 1
        r = 2 * i + 2
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            maxNumber = i
            if l < size and A[i] < A[l]:
                maxNumber = l
            if r < size and A[maxNumber] < A[r]:
                maxNumber = r
            if maxNumber != i:
                A[maxNumber], A[i] = A[i], A[maxNumber]
                i = maxNumber
            else:
                break

    