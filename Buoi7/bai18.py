class Queue:
    def __init__(self):
        self.items = []  # Mảng động lưu trữ dữ liệu
    
    def enqueue(self, x):
        self.items.append(x)  # Thêm vào cuối hàng đợi
    
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

def mo_phong_queue(day_lenh):
    q = Queue()
    for lenh in day_lenh:
        if lenh.startswith("enqueue"):
            so = int(lenh.split()[1])
            q.enqueue(so)
        elif lenh == "dequeue":
            if not q.isEmpty():
                print("In giá trị dequeue:", q.dequeue())
    print("Trạng thái Queue cuối cùng:", q.items)

mo_phong_queue(["enqueue 5", "enqueue 7", "dequeue"])