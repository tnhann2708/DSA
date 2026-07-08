class DanhSachMangDong:

    def __init__(self):

        self.suc_chua = 2
        self.so_phan_tu = 0
        self.mang = [None] * self.suc_chua

    def mo_rong(self):

        self.suc_chua *= 2

        mang_moi = [None] * self.suc_chua

        for i in range(self.so_phan_tu):
            mang_moi[i] = self.mang[i]

        self.mang = mang_moi

    def them(self, gia_tri):

        if self.so_phan_tu == self.suc_chua:
            self.mo_rong()

        self.mang[self.so_phan_tu] = gia_tri
        self.so_phan_tu += 1

    def hien_thi(self):

        for i in range(self.so_phan_tu):
            print(self.mang[i], end=" ")

        print()


ds = DanhSachMangDong()

for i in range(1, 11):
    ds.them(i)

ds.hien_thi()

print("Sức chứa:", ds.suc_chua)