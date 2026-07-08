class DanhSachMang:

    def __init__(self):
        self.du_lieu = []

    def xoa_so_chan(self):

        ket_qua = []

        for i in self.du_lieu:

            if i % 2 != 0:
                ket_qua.append(i)

        self.du_lieu = ket_qua

    def hien_thi(self):
        print(self.du_lieu)


ds = DanhSachMang()

ds.du_lieu = [1, 2, 3, 4]

ds.xoa_so_chan()

ds.hien_thi()