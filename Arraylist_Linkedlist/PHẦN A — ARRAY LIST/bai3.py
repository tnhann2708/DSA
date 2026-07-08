class DanhSachMang:

    def __init__(self):
        self.du_lieu = []

    def chen(self, vi_tri, gia_tri):
        self.du_lieu.insert(vi_tri, gia_tri)

    def xoa(self, vi_tri):

        if 0 <= vi_tri < len(self.du_lieu):
            self.du_lieu.pop(vi_tri)

    def hien_thi(self):
        print(self.du_lieu)


ds = DanhSachMang()
ds.du_lieu = [1, 2, 4]

print("Ban đầu:")
ds.hien_thi()
ds.chen(2, 3)

print("Sau khi chèn:")
ds.hien_thi()
ds.xoa(1)

print("Sau khi xóa:")
ds.hien_thi()