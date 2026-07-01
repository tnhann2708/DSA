class PriorityQueueDonGian:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue_min(self):
        if len(self.items) == 0: return None
        min_idx = 0
        for i in range(len(self.items)):
            if self.items[i] < self.items[min_idx]:
                min_idx = i
        return self.items.pop(min_idx)

pq = PriorityQueueDonGian()
pq.enqueue(30); pq.enqueue(10); pq.enqueue(20)
print("Lấy phần tử ưu tiên cao nhất (Min):", pq.dequeue_min())