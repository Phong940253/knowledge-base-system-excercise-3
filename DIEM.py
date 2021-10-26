
class DIEM:
    def __init__(self, x, y, ten):
        self.x = x
        self.y = y
        # thuộc tính tạo độ
        self.ten = ten
        # thuộc tính tên

    def __eq__(self, DIEM):
        return self.x == DIEM.x and self.y == DIEM.y
        # quan hệ điểm trùng điểm
