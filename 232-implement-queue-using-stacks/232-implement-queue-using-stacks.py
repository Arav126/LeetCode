class MyQueue:

    def __init__(self):
        self.s = []
        

    def push(self, x: int) -> None:
        self.s.append(x)
        
        

    def pop(self) -> int:
        j = self.s.pop(0)
        return j
        

    def peek(self) -> int:
        return self.s[0]
        

    def empty(self) -> bool:
        return len(self.s)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()