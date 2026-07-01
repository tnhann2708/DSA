class QueueTuHaiStack:
    def __init__(self):
        self.in_stack = [] 
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        # Nếu out_stack rỗng, đổ hết từ in_stack sang out_stack
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())
        
        if len(self.out_stack) == 0:
            print("Hàng đợi rỗng!")
            return None
        return self.out_stack.pop()

q_2st = QueueTuHaiStack()
q_2st.enqueue("A"); q_2st.enqueue("B")
print("Dequeue:", q_2st.dequeue())