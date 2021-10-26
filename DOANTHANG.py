class DOANTHANG:
    def __init__(self, ten, diem1, diem2):
        self.diem1 = diem1
        # thuộc tính điểm 1
        self.diem2 = diem2
        # thuộc tính điểm 2
        self.ten = ten
        # thuộc tính tên

    def __eq__(self, DIEM) -> bool:
        return self.diem1 == DIEM.diem1 and self.diem2 == DIEM.diem2
        # quan hệ đoạn thẳng trùng đoạn thẳng
