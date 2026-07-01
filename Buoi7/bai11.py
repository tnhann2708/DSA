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
    
def phan_tu_lon_hon_ke_tiep(mang_a):
    n = len(mang_a)
    kq = [-1] * n
    st = Stack()
    
    for i in range(n - 1, -1, -1):
        while not st.isEmpty() and st.top() <= mang_a[i]:
            st.pop()
        if not st.isEmpty():
            kq[i] = st.top()
        st.push(mang_a[i])
    return kq

mang_test = [2, 1, 3]
print(f"Mảng gốc: {mang_test} -> Kết quả lớn hơn kề bên:", phan_tu_lon_hon_ke_tiep(mang_test))