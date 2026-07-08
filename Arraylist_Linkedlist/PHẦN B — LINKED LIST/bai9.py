class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


def hien_thi(dau):

    while dau:

        print(dau.du_lieu, end=" -> ")

        dau = dau.tiep

    print("null")


def tron(a, b):

    gia = Nut(0)

    hien_tai = gia

    while a and b:

        if a.du_lieu < b.du_lieu:

            hien_tai.tiep = a
            a = a.tiep

        else:

            hien_tai.tiep = b
            b = b.tiep

        hien_tai = hien_tai.tiep

    if a:
        hien_tai.tiep = a

    else:
        hien_tai.tiep = b

    return gia.tiep


a = Nut(1)
b = Nut(3)
c = Nut(5)

a.tiep = b
b.tiep = c

d = Nut(2)
e = Nut(4)

d.tiep = e

kq = tron(a, d)

hien_thi(kq)