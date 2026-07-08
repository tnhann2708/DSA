class DanhSachMang:

    def __init__(self):
        self.du_lieu = []

    def dao_nguoc(self):
        trai = 0
        phai = len(self.du_lieu) - 1

        while trai < phai:
            self.du_lieu[trai], self.du_lieu[phai] = (self.du_lieu[phai], self.du_lieu[trai])
            trai += 1
            phai -= 1

    def hien_thi(self):
        print(self.du_lieu)


ds = DanhSachMang()

ds.du_lieu = [1, 2, 3, 4]

ds.dao_nguoc()
ds.hien_thi()