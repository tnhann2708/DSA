class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


def hien_thi(dau):

    while dau:

        print(dau.du_lieu, end=" -> ")

        dau = dau.tiep

    print("null")


def xoa_k(dau, k):

    ds = []

    hien_tai = dau

    while hien_tai:

        ds.append(hien_tai)

        hien_tai = hien_tai.tiep

    xoa = len(ds) - k

    if xoa == 0:

        return dau.tiep

    ds[xoa - 1].tiep = ds[xoa].tiep

    return dau


a = Nut(1)
b = Nut(2)
c = Nut(3)
d = Nut(4)
e = Nut(5)

a.tiep = b
b.tiep = c
c.tiep = d
d.tiep = e

a = xoa_k(a, 2)

hien_thi(a)