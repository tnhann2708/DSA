class CircularQueue:
    def __init__(self, dung_luong):
        self.n = dung_luong
        self.items = [None] * dung_luong
        self.head = 0 
        self.tail = 0 
        self.size = 0

    def isFull(self):
        return self.size == self.n

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, x):
        if self.isFull():
            print("Hàng đợi đầy!")
            return
        self.items[self.tail] = x
        self.tail = (self.tail + 1) % self.n  # Quay vòng chỉ số tail
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Hàng đợi rỗng!")
            return None
        val = self.items[self.head]
        self.items[self.head] = None  # Xoá dữ liệu cũ
        self.head = (self.head + 1) % self.n  # Quay vòng chỉ số head
        self.size -= 1
        return val

cq = CircularQueue(3)
cq.enqueue(10); cq.enqueue(20); cq.enqueue(30)
print("Lấy ra:", cq.dequeue())
cq.enqueue(40)
print("Mảng nội bộ hiện tại:", cq.items)