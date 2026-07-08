class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


def sap_xep(dau):

    ds = []

    while dau:

        ds.append(dau.du_lieu)

        dau = dau.tiep

    ds.sort()

    return ds


a = Nut(3)
b = Nut(1)
c = Nut(2)

a.tiep = b
b.tiep = c

print(sap_xep(a))