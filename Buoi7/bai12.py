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

def hcn_lon_nhat_histogram(h):
    st = Stack()
    max_area = 0
    i = 0
    while i < len(h):
        if st.isEmpty() or h[i] >= h[st.top()]:
            st.push(i)
            i += 1
        else:
            top_idx = st.pop()
            rong = i if st.isEmpty() else (i - st.top() - 1)
            max_area = max(max_area, h[top_idx] * rong)
            
    while not st.isEmpty():
        top_idx = st.pop()
        rong = i if st.isEmpty() else (i - st.top() - 1)
        max_area = max(max_area, h[top_idx] * rong)
    return max_area

cot_histogram = [2, 1, 5, 6, 2, 3]
print("Diện tích lớn nhất tìm được:", hcn_lon_nhat_histogram(cot_histogram))