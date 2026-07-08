class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


def chen_sau(nut, gia_tri):

    nut_moi = Nut(gia_tri)

    nut_moi.tiep = nut.tiep

    nut.tiep = nut_moi


def hien_thi(dau):

    while dau:

        print(dau.du_lieu, end=" -> ")

        dau = dau.tiep

    print("null")


a = Nut(1)

b = Nut(3)

a.tiep = b

chen_sau(a, 2)

hien_thi(a)