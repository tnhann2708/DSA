class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


def co_chu_trinh(dau):

    rua = dau
    tho = dau

    while tho and tho.tiep:

        rua = rua.tiep
        tho = tho.tiep.tiep

        if rua == tho:
            return True

    return False


a = Nut(1)
b = Nut(2)
c = Nut(3)

a.tiep = b
b.tiep = c
c.tiep = a

print(co_chu_trinh(a))