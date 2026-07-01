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
    
def tinh_bieu_thuc_hau_to(bieu_thuc_mang):
    st = Stack()
    for ky_tu in bieu_thuc_mang:
        if ky_tu.isdigit():
            st.push(int(ky_tu))
        else:
            so_2 = st.pop()
            so_1 = st.pop()
            if ky_tu == '+': st.push(so_1 + so_2)
            elif ky_tu == '-': st.push(so_1 - so_2)
            elif ky_tu == '*': st.push(so_1 * so_2)
            elif ky_tu == '/': st.push(int(so_1 / so_2))
    return st.pop()

bieu_thuc = ["3", "4", "+", "2", "*"] 
print("Kết quả tính hậu tố:", tinh_bieu_thuc_hau_to(bieu_thuc))  