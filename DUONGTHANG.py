class DUONGTHANG:
    def __init__(self, a, b, c, ten):
        self.a = a
        self.b = b
        self.c = c
        # thuộc tính a b c của phương trình đường thẳng ax + by + c = 0
        self.ten = ten
        # thuộc tính tên

    def __eq__(self, DUONGTHANG):
        return self.a == DUONGTHANG.a and self.b == DUONGTHANG.b and self.c == DUONGTHANG.c
        # quam hệ đường thẳng trùng đường thẳng
