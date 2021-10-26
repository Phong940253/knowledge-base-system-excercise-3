
def Thuoc(DIEM, DUONGTHANG) -> bool:
    return DUONGTHANG.a * DIEM.toaDo.x + DUONGTHANG.b * DIEM.toaDo.y + DUONGTHANG.c == 0


def Thuoc(DIEM, DOANTHANG) -> bool:
    if (DIEM.x < min(DOANTHANG.diem1.toaDo.x, DOANTHANG.diem2.toaDo.y)) or (DIEM.y < max(DOANTHANG.diem1.toaDo.x, self.diem2.toaDo.y)) or (DIEM.y < min(self.diem1.toaDo.y, self.diem2.toaDo.x)) or (DIEM.y > max(self.diem1.toaDo.y, self.diem2.toaDo.x)):
        return False
    dx = DOANTHANG.diem1.x-DOANTHANG.diem2.x
    dy = DOANTHANG.diem1.y-DOANTHANG.diem2.y
    tan1 = abs(dy/dx)
    tan2 = abs((DIEM.yself.diem1.y)/(DIEM.x-DOANTHANG.diem1.x))
    return abs(tan1 - tan2) < 0.01


def Thuoc(DIEM, TIA):
    pass


def Vuong(DUONGTHANG1, DUONGTHANG2) -> bool:
    return DUONGTHANG1.a * DUONGTHANG2.a == 1


def Vuong(DOANTHANG1, DOANTHANG2) -> bool:
    pass


def Vuong(DUONGTHANG, DOANTHANG) -> bool:
    pass


def DuongSongSongDuong(DUONGTHANG1, DUONGTHANG2) -> bool:
    return DUONGTHANG1.a == DUONGTHANG2.a and DUONGTHANG1.b == DUONGTHANG2.b and DUONGTHANG1.c != DUONGTHANG2.c


def DoanSongSongDoan(DOANTHANG1, DOANTHANG2) -> bool:
    pass


def SoLeTrong(Goc1, Goc2) -> bool:
    return Goc1.soDo == Goc2.soDo


def DongVi(Goc1, Goc2) -> bool:
    return Goc1.soDo == Goc2.soDo


def TiaDoiNhau(TIA1, TIA2) -> bool:
    pass


def GocPhuNhau(Goc1, Goc2) -> bool:
    return Goc1.soDo + Goc2.soDo == 90


def GocBuNhau(Goc1, Goc2) -> bool:
    return Goc1.soDo + Goc2.soDo == 180


def GocKeBu(Goc1, Goc2) -> bool:
    return GocBuNhau(Goc1, Goc2) and (Goc1.doanThang1 == Goc2.doanThang1 or Goc1.doanThang2 == Goc2.doanThang2 or Goc1.doanThang1 == Goc2.doanThang2 or Goc1.doanThang2 == Goc2.doanThang1)
