class DanhSachMang:

    def __init__(self):
        self.du_lieu = []

    def them_cuoi(self, gia_tri):
        self.du_lieu.append(gia_tri)

    def xoa_cuoi(self):
        if self.du_lieu:
            return self.du_lieu.pop()
        return None

    def hien_thi(self):
        print(self.du_lieu)
        
ds = DanhSachMang()

ds.them_cuoi(1)
ds.them_cuoi(2)
ds.them_cuoi(3)

ds.hien_thi()

print("popBack: ", ds.xoa_cuoi())
ds.hien_thi()