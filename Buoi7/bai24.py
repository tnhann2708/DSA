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
    
def duyet_bfs(do_thi, dinh_goc):
    hang_doi = Queue()
    hang_doi.enqueue(dinh_goc)
    da_tham = [dinh_goc]
    thu_tu_tham = []

    while not hang_doi.isEmpty():
        u = hang_doi.dequeue()
        thu_tu_tham.append(u)
        for v in do_thi.get(u, []):
            if v not in da_tham:
                da_tham.append(v)
                hang_doi.enqueue(v)
    return thu_tu_tham

do_thi_mau = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}
print("Thứ tự thăm BFS:", duyet_bfs(do_thi_mau, 'A'))