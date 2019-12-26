# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val=[]
        self.index=-1
        

    def push(self, x: int) -> None:       # push
        self.val.append(x)
        self.index+=1
        

    def pop(self) -> None:                # pop
        self.val.pop()
        self.index-=1
        

    def top(self) -> int:                 #top
        return self.val[self.index]
        

    def getMin(self) -> int:              # 找到最小元素
        return min(self.val)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
