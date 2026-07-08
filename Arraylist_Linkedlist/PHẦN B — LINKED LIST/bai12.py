class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


def bat_dau(dau):

    da_di = []

    while dau:

        if dau in da_di:

            return dau.du_lieu

        da_di.append(dau)

        dau = dau.tiep


a = Nut(1)
b = Nut(2)
c = Nut(3)

a.tiep = b
b.tiep = c
c.tiep = b

print(bat_dau(a))