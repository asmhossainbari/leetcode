class CustomStack(object):
    
    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.list = []
        self.max_size = maxSize
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.list) < self.max_size:
            self.list.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.list) > 0:
            return self.list.pop()
        else:
            return -1

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if len(self.list) >= k:
            for i in range(k):
                self.list[i] += val
        else:
            for i in range(len(self.list)):
                self.list[i] += val

    def getList(self):
        return self.list
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


customStack = CustomStack(3)
customStack.push(1)
customStack.push(2)
print(customStack.pop())
# print(customStack.getList())
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.increment(5,100)
customStack.increment(2,100)
print(customStack.pop())
# print(customStack.getList())
print(customStack.pop())
# print(customStack.getList())
print(customStack.pop())
# print(customStack.getList())
print(customStack.pop())
# print(customStack.getList())
