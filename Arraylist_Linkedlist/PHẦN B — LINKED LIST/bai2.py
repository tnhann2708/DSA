class Nut:

    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.tiep = None


class DanhSachLienKet:

    def __init__(self):
        self.dau = None

    def dem(self):

        dem = 0
        hien_tai = self.dau

        while hien_tai:

            dem += 1
            hien_tai = hien_tai.tiep

        return dem

    def hien_thi(self):

        hien_tai = self.dau

        while hien_tai:

            print(hien_tai.du_lieu)

            hien_tai = hien_tai.tiep


ds = DanhSachLienKet()

a = Nut(1)
b = Nut(2)
c = Nut(3)

ds.dau = a
a.tiep = b
b.tiep = c
ds.hien_thi()

print("Độ dài:", ds.dem())