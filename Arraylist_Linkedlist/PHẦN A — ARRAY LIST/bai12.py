class DanhSachMang:
    
    def xoa_trung(self, arr):
        
        da_co = set()
        ket_qua = []
        
        for i in arr:
            if i not in da_co:
                ket_qua.append(i)
                da_co.add(i)
                
        return ket_qua
    
ds = DanhSachMang()
print(ds.xoa_trung([3, 1, 3, 2, 1]))
