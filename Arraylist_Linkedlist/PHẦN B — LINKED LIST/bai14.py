class Nut:

    def __init__(self, du_lieu):

        self.du_lieu = du_lieu
        self.tiep = None


def hien_thi(dau):

    while dau:

        print(dau.du_lieu, end=" -> ")

        dau = dau.tiep

    print("null")


def cong(a, b):

    tong = []
    nho = 0

    while a or b or nho:

        x = a.du_lieu if a else 0
        y = b.du_lieu if b else 0

        s = x + y + nho

        tong.append(s % 10)

        nho = s // 10

        a = a.tiep if a else None
        b = b.tiep if b else None

    dau = Nut(tong[0])
    hien_tai = dau

    for i in tong[1:]:

        hien_tai.tiep = Nut(i)
        hien_tai = hien_tai.tiep

    return dau


a=Nut(2)
b=Nut(4)
c=Nut(3)

a.tiep=b
b.tiep=c

d=Nut(5)
e=Nut(6)
f=Nut(4)

d.tiep=e
e.tiep=f

hien_thi(cong(a,d))