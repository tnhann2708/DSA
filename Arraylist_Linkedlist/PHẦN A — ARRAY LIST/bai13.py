class DanhSachKhoang:

    def tron_khoang(self, ds):

        ds.sort()

        ket_qua = [ds[0]]

        for i in ds[1:]:

            cuoi = ket_qua[-1]

            if i[0] <= cuoi[1]:

                cuoi[1] = max(cuoi[1], i[1])

            else:

                ket_qua.append(i)

        return ket_qua


obj = DanhSachKhoang()

print(obj.tron_khoang([[1, 3], [2, 6], [8, 10]]))