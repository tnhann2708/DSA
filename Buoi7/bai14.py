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

def tinh_nhip_gia_co_phieu(gia):
    n = len(gia)
    nhip = [0] * n
    st = Stack()
    
    for i in range(n):
        while not st.isEmpty() and gia[st.top()] <= gia[i]:
            st.pop()
        nhip[i] = (i + 1) if st.isEmpty() else (i - st.top())
        st.push(i)
    return nhip

mang_gia = [100, 80, 60, 70, 60, 75, 85]
print("Nhịp giá tương ứng từng ngày:", tinh_nhip_gia_co_phieu(mang_gia)) 