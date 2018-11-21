class Solution:
    def printListFromTailToHead(self, listNode):
        # write code here
        stack = []
        res = []
        if listNode == None:
            return res
        while listNode != None:
            stack.append(listNode.val)
            listNode = listNode.next
        while len(stack) != 0:
            res.append(stack.pop())
        return res
        