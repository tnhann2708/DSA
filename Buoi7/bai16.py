class Queue:
    def __init__(self):
        self.items = []  # Mảng động lưu trữ dữ liệu
    
    def enqueue(self, x):
        self.items.append(x)  # Thêm vào cuối hàng đợi
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Underflow")
        return self.items.pop(0)
    
    def front(self):
        if self.isEmpty():
            raise IndexError("Hàng đợi rỗng")
        return self.items[0]
    def isEmpty(self):
        return len(self.items) == 0
    
q1 = Queue()
q1.enqueue(1); q1.enqueue(2); q1.enqueue(3)
print("Dequeue lần đầu (ra số 1):", q1.dequeue())