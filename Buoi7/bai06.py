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

def kiem_tra_ngoac_can_bang(chuoi_ngoac):
    st = Stack()
    for ky_tu in chuoi_ngoac:
        if ky_tu in ['(', '[', '{']:
            st.push(ky_tu)
        else:
            if st.isEmpty(): 
                return False
            top_val = st.pop()
            if ky_tu == ')' and top_val != '(': return False
            if ky_tu == ']' and top_val != '[': return False
            if ky_tu == '}' and top_val != '{': return False
    return st.isEmpty()

print("Chuỗi '([]{})' cân bằng?:", kiem_tra_ngoac_can_bang("([]{})"))
print("Chuỗi '([)]' cân bằng?:", kiem_tra_ngoac_can_bang("([)]"))