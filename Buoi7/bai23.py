class Deque:
    def __init__(self):
        self.items = []

    def pushFront(self, x):
        self.items.insert(0, x)

    def pushBack(self, x):
        self.items.append(x)

    def popFront(self):
        if len(self.items) == 0: return None
        return self.items.pop(0)

    def popBack(self):
        if len(self.items) == 0: return None
        return self.items.pop()

dq = Deque()
dq.pushFront(1); dq.pushBack(2)
print("Mảng Deque:", dq.items)