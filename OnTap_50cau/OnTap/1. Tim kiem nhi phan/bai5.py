import math

def toc_do_an(chuoi, h):

    toc_do = 1

    while True:

        tong = 0

        for so in chuoi:
            tong += math.ceil(so / toc_do)

        if tong <= h:
            return toc_do

        toc_do += 1


print(toc_do_an([3,6,7,11],8))