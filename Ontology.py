from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")


class TOADO(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o) and self.x == o.x and self.y == o.y


def parser(x, y):
    return TOADO(x, y)


def unparser(v):
    return v[0], v[1]


declare_datatype(TOADO, "", parser, unparser)


with onto:
    # OBJECT PROPERTIES

    class DIEM(Thing):
        pass

    class has_TOADO(DIEM >> TOADO, FunctionalProperty):
        python_name = "toaDo"

    class DIEM(Thing):
        defined_class = True
        has_TOADO = [TOADO]

        def trung_diem(self, DIEM):
            return self.toaDo == DIEM.toaDo

    class DOANTHANG(Thing):
        pass

    class DOANTHANG_has_DIEM(DOANTHANG >> DIEM, FunctionalProperty):
        python_name = "doanThang"

    class DOANTHANG(Thing):
        defined_class = True
        DOANTHANG_has_DIEM = [DIEM]

    class DUONGTHANG(Thing):
        pass

    class DUONGTHANG_has_DIEM(DUONGTHANG >> DIEM, FunctionalProperty):
        python_name = "duongThang"

    class has_DOANTHANG(DUONGTHANG >> DOANTHANG, FunctionalProperty):
        python_name = "doanThang"

    class DUONGTHANG(Thing):
        defined_class = True
        DUONGTHANG_has_DIEM = [DIEM]
        has_DOANTHANG = [DOANTHANG]

    class TIA(Thing):
        pass

    class TIA_has_DIEM(TIA >> DIEM):
        pass

    class TIA(Thing):
        defined_class = True
        TIA_has_DIEM = [DIEM]

# print(onto.classes())
onto.save(file="onto")
