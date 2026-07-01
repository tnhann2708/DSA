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
    
def do_uu_tien(toan_tu):
    if toan_tu in ['+', '-']: return 1
    if toan_tu in ['*', '/']: return 2
    return 0

def trung_to_sang_hau_to(chuoi_trung_to):
    st = Stack()
    ket_qua = ""
    for ky_tu in chuoi_trung_to:
        if ky_tu.isalnum():
            ket_qua += ky_tu
        elif ky_tu == '(':
            st.push(ky_tu)
        elif ky_tu == ')':
            while not st.isEmpty() and st.top() != '(':
                ket_qua += st.pop()
            st.pop()
        else:
            while not st.isEmpty() and do_uu_tien(st.top()) >= do_uu_tien(ky_tu):
                ket_qua += st.pop()
            st.push(ky_tu)
    while not st.isEmpty():
        ket_qua += st.pop()
    return ket_qua

print("Hậu tố của 'a+b*c' là:", trung_to_sang_hau_to("a+b*c"))