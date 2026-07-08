class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


class DanhSachLienKet:

    def __init__(self):

        self.dau = None

    def tim(self, gia_tri):

        vi_tri = 0

        hien_tai = self.dau

        while hien_tai:

            if hien_tai.du_lieu == gia_tri:

                return vi_tri

            vi_tri += 1

            hien_tai = hien_tai.tiep

        return -1


ds = DanhSachLienKet()

a = Nut(1)
b = Nut(2)
c = Nut(3)

ds.dau = a
a.tiep = b
b.tiep = c

print(ds.tim(2))