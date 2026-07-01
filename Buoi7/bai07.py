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
    
class MinStack:
    def __init__(self):
        self.data = Stack()
        self.data_min = Stack()

    def push(self, x):
        self.data.push(x)
        if self.data_min.isEmpty() or x <= self.data_min.top():
            self.data_min.push(x)
        else:
            self.data_min.push(self.data_min.top())

    def pop(self):
        self.data_min.pop()
        return self.data.pop()

    def getMin(self):
        return self.data_min.top()

min_st = MinStack()
min_st.push(5); min_st.push(3); min_st.push(7)
print("Giá trị nhỏ nhất hiện tại là:", min_st.getMin())