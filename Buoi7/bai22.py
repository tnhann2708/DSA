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
    
def dao_nguoc_queue(q_goc):
    stack_tam = []

    while not q_goc.isEmpty():
        stack_tam.append(q_goc.dequeue())

    while len(stack_tam) > 0:
        q_goc.enqueue(stack_tam.pop())

q7 = Queue()
q7.enqueue(1); q7.enqueue(2); q7.enqueue(3)
print("Queue sau khi đảo ngược:", q7.items)