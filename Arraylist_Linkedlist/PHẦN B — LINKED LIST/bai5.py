class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


def xoa(dau, x):

    if dau and dau.du_lieu == x:

        return dau.tiep

    hien_tai = dau

    while hien_tai.tiep:

        if hien_tai.tiep.du_lieu == x:

            hien_tai.tiep = hien_tai.tiep.tiep

            break

        hien_tai = hien_tai.tiep

    return dau


def hien_thi(dau):

    while dau:

        print(dau.du_lieu, end=" -> ")

        dau = dau.tiep

    print("null")


a = Nut(1)
b = Nut(2)
c = Nut(3)
d = Nut(2)

a.tiep = b
b.tiep = c
c.tiep = d

a = xoa(a, 2)

hien_thi(a)