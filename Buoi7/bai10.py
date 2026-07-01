class StackBangHaiQueue:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q2.append(x)
        while len(self.q1) > 0:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if len(self.q1) == 0: 
            raise IndexError("Stack rỗng")
        return self.q1.pop(0)

st_queue = StackBangHaiQueue()
st_queue.push(10); st_queue.push(20)
print("Pop từ ngăn xếp mô phỏng bằng queue:", st_queue.pop())