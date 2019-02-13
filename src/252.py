# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        startList = []
        endList = []
        for s in intervals:
            startList.append(s.start)
            endList.append(s.end)
        
        startList.sort()
        endList.sort()
        
        for i in range(1, len(intervals)):
            if startList[i] < endList[i - 1]:
                return False
        return True


'''
这是很典型的一类问题：
sorted events according to start time:

我们只关心开始时间和结束时间，让它们排序，使用容器中元素的数量来进行判断；
通过遍历时间，根据两个时间的差值来改变容器状态，通过状态来进行条件判断；

intervals time --> greedy

排序之后对我们的结果没有影响，因为可以转化为人进入房间的问题； 我们不需要知道
每一个人进去出去的时间，我们只需要在某一个时刻有人进入，有人出去，通过他们的关系
去判断。


'''