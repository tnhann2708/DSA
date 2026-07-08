class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


class DanhSachLienKet:

    def __init__(self):
        self.dau = None

    def them_dau(self, gia_tri):

        nut_moi = Nut(gia_tri)
        nut_moi.tiep = self.dau
        self.dau = nut_moi

    def them_cuoi(self, gia_tri):

        nut_moi = Nut(gia_tri)

        if self.dau is None:

            self.dau = nut_moi
            return

        hien_tai = self.dau

        while hien_tai.tiep:

            hien_tai = hien_tai.tiep

        hien_tai.tiep = nut_moi

    def hien_thi(self):

        hien_tai = self.dau

        while hien_tai:

            print(hien_tai.du_lieu, end=" -> ")

            hien_tai = hien_tai.tiep

        print("null")


ds = DanhSachLienKet()

ds.them_dau(2)
ds.them_cuoi(5)
ds.hien_thi()