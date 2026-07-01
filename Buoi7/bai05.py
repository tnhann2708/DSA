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

def duyet_va_dem_phan_tu(stack_goc):
    stack_phu = Stack()
    dem = 0
    
    print("Các phần tử in theo thứ tự LIFO là:")
    
    while not stack_goc.isEmpty():
        gia_tri = stack_goc.pop()
        print(gia_tri)
        dem += 1
        stack_phu.push(gia_tri)
        
    while not stack_phu.isEmpty():
        stack_goc.push(stack_phu.pop())
        
    return dem

s = Stack()
s.push(1)
s.push(2)
s.push(3)

tong_so_phan_tu = duyet_va_dem_phan_tu(s)
print(f"Tổng số phần tử đếm được: {tong_so_phan_tu}")
print("Trạng thái mảng items bên trong sau khi đếm (vẫn giữ nguyên):", s.items)