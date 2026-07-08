class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


def tim_giua(dau):

    cham = dau
    nhanh = dau

    while nhanh and nhanh.tiep:

        cham = cham.tiep
        nhanh = nhanh.tiep.tiep

    return cham.du_lieu


a=Nut(1)
b=Nut(2)
c=Nut(3)
d=Nut(4)
e=Nut(5)

a.tiep=b
b.tiep=c
c.tiep=d
d.tiep=e

print("Nut giua:", tim_giua(a))