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

def sap_xep_ngan_xep(st_goc):
    st_phu = Stack()
    
    while not st_goc.isEmpty():
        temp = st_goc.pop()
        while not st_phu.isEmpty() and st_phu.top() > temp:
            st_goc.push(st_phu.pop())
        st_phu.push(temp)
        
    while not st_phu.isEmpty():
        st_goc.push(st_phu.pop())

st_test = Stack()
st_test.push(3); st_test.push(1); st_test.push(2)
print("Mảng items gốc bên trong:", st_test.items)
sap_xep_ngan_xep(st_test)
print("Mảng items bên trong sau khi sắp xếp (đỉnh nhỏ nhất):", st_test.items)