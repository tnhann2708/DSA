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

def dfs_khong_de_quy(do_thi, dinh_dau):
    st = Stack()
    st.push(dinh_dau)
    da_tham = set()
    kq_duyet = []
    
    while not st.isEmpty():
        u = st.pop()
        if u not in da_tham:
            da_tham.add(u)
            kq_duyet.append(u)
            for v in reversed(do_thi.get(u, [])):
                if v not in da_tham:
                    st.push(v)
    return kq_duyet

do_thi_mau = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}
print("Thứ tự duyệt DFS từ đỉnh A:", dfs_khong_de_quy(do_thi_mau, 'A'))