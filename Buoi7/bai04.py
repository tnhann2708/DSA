class StackBai4:
    def __init__(self, dung_luong_toi_da):
        self.items = []
        self.dung_luong = dung_luong_toi_da  # Giới hạn kích thước của ngăn xếp
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def isFull(self):
        return len(self.items) == self.dung_luong

    def push(self, x):
        if self.isFull():
            print(f"Lỗi: Không thể push {x}. Ngăn xếp đã đầy! (Overflow)")
            return
        self.items.append(x)
        print(f"Push thành công: {x}")
    
    def pop(self):
        if self.isEmpty():
            print("Lỗi: Không thể pop. Ngăn xếp đang rỗng! (Underflow)")
            return None
        return self.items.pop()
    
    def top(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng!")
            return None
        return self.items[-1]

s = StackBai4(dung_luong_toi_da=2)

s.push(10) 
s.push(20)  
s.push(30)

print("Các phần tử trong stack:", s.items)

print("Pop lần 1:", s.pop())
print("Pop lần 2:", s.pop())
print("Pop lần 3:", s.pop())