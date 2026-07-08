class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


def dao_nguoc(dau):

    truoc = None
    hien_tai = dau

    while hien_tai:

        sau = hien_tai.tiep
        hien_tai.tiep = truoc
        truoc = hien_tai
        hien_tai = sau

    return truoc


def hien_thi(dau):

    while dau:

        print(dau.du_lieu, end=" -> ")

        dau = dau.tiep

    print("null")

a = Nut(1)
b = Nut(2)
c = Nut(3)

a.tiep = b
b.tiep = c

print("Trước khi đảo:")
hien_thi(a)

a = dao_nguoc(a)

print("Sau khi đảo:")
hien_thi(a)