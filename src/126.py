class Solution:
    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        hashSet = set(wordList)
        queue = collections.deque([beginWord])
        visited = set([beginWord])
        distance = 0
        
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return distance
                for next_word in self.get_next_word(word):
                    if next_word not in hashSet or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
                    
        return 0
    
    def get_next_word(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
                
        return words

'''
这是一个比较好的bfs的习题：为什么：

求最短距离

使用的解体思路和之前的bfs相同，需要的数据结构有set，queue

这里set一个是为了判断有没有visited，另一个是判断在不在原来的
列表中。

这里比较tricky的一个地方是如何获取下一个words的list，这里使用
两个list去合并。

每次for循环中会判断queue中出队的元素有没有被访问过
'''