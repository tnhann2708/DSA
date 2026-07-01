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

def mo_phong_day_thao_tac(day_lenh):
    s = Stack()

    for lenh in day_lenh:
        if lenh.startswith("push"):
            gia_tri = int(lenh.split()[1])
            s.push(gia_tri)
            print(f"Thực hiện: {lenh}")
            
        elif lenh == "pop":
            if not s.isEmpty():
                val = s.pop()
                print(f"Thực hiện: pop -> Giá trị in ra: {val}")
            else:
                print("Thực hiện: pop -> Lỗi Underflow (Stack rỗng)!")
                
    print("\nTrạng thái ngăn xếp cuối cùng (Từ đáy lên đỉnh):", s.items)

day_lenh_1 = ["push 5", "push 7", "pop"]
print("Mẫu dữ liệu 1:")
mo_phong_day_thao_tac(day_lenh_1)

day_lenh_2 = ["push 10", "push 20", "pop", "push 30", "push 40", "pop"]
print("Mẫu dữ liệu 2:")
mo_phong_day_thao_tac(day_lenh_2)