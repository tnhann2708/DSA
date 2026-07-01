class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("Underflow")
        return self.items.pop()
    
    def top(self):
        if self.isEmpty():
            raise IndexError("danh sách rỗng")
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Phần tử vừa pop ra:", s.pop())
print("Phần tử đang ở đỉnh:", s.top())
print("Stack có rỗng không?:", s.isEmpty())