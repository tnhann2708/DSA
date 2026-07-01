class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, x):
        self.items.append(x)
    
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
    
def in_front_rear(q_goc):
    if len(q_goc.items) == 0:
        print("Hàng đợi rỗng")
        return
    dau_hang = q_goc.items[0]
    cuoi_hang = q_goc.items[-1]
    print(f"front = {dau_hang}, rear = {cuoi_hang}")

q5 = Queue()
q5.enqueue(4); q5.enqueue(5); q5.enqueue(6)
in_front_rear(q5)