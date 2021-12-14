def diem_diem(match):
    if match.group(2).casefold() == "nằm giữa":
        return (match.group(1) + " " + match.group(2) + " " + match.group(3) +
                "," + match.group(4))
    else:
        return match.group(1) + " " + match.group(2)


def diem_duong(match):
    return match.group(1) + " " + match.group(2) + " " + match.group(3)


def diem_doan(match):
    if match.group(2).casefold() == "là giao điểm":
        return (match.group(1) + " " + match.group(2) + " của " +
                match.group(3) + " và " + match.group(4))
    elif match.group(2).casefold() == "là trung điểm":
        return match.group(1) + " " + match.group(2) + " của " + match.group(3)
    else:
        return match.group(1) + " " + match.group(2) + " " + match.group(3)


def diem_doan_extra(match):
    return match.group(1) + " " + match.group(3) + " của " + match.group(
        4) + ";" + match.group(2) + " " + match.group(
            3) + " của " + match.group(5)


def diem_tia(match):
    if "thuộc" in match.group(2).casefold():
        return match.group(1) + " thuộc Tia(" + match.group(3) + ")"
    else:
        return (match.group(1) + " là giao điểm của " + match.group(4) + "(" +
                match.group(5) + ") và " + match.group(6) + "(" +
                match.group(7) + ")")


def diem_tron(match):
    return (match.group(1) + " " + match.group(2) + " đường tròn tâm " +
            match.group(4) + " bán kính " + match.group(5))


def doan_tron(match):
    return (match.group(1) + " là " + match.group(2) + " đường tròn tâm " +
            match.group(4) + " bán kính " + match.group(5))


def diem_doan_tron(match):
    if "đoạn thẳng" in match.group(2).casefold():
        return (match.group(1) + " là giao điểm của " + match.group(3) +
                " và đường tròn tâm" + match.group(8) + " bán kính " +
                match.group(9))
    else:
        return (match.group(1) + " là giao điểm của " + match.group(7) +
                " và đường tròn tâm" + match.group(4) + " bán kính " +
                match.group(5))


def doan_doan(match):
    if match.group(2).casefold() == "vuông":
        return match.group(1) + " vuông góc " + match.group(3)
    elif match.group(2).casefold() == "bằng":
        return match.group(1) + " = " + match.group(3)
    else:
        return match.group(0)


def doan_giao_diem(match):
    return (match.group(1) + " là giao điểm của " + match.group(2) + " và " +
            match.group(3))


def tia_nam_giua(match):
    return ("Tia(" + match.group(2) + ") nằm giữa Tia(" + match.group(4) +
            "),Tia(" + match.group(6) + ")")


def tia_doi_nhau(match):
    return "Tia(" + match.group(2) + ") đối Tia(" + match.group(4) + ")"


def diem_tia_doan(match):
    return ("Điểm " + match.group(1) + " " + match.group(2) + " " +
            match.group(3) + "(" + match.group(4) + ") và " + match.group(5) +
            "(" + match.group(6) + ")")


def doan_tam_giac(match):
    return match.group(0)


def doan_tu_giac(match):
    return match.group(0)


def goc_goc(match):
    if match.group(2) in ["=", "bằng"]:
        return "Góc(" + match.group(1) + ") = góc(" + match.group(4) + ")"
    else:
        return "Góc(" + match.group(1) + ") là góc vuông"


def goc_doan_tia(match):
    if match.group(2).casefold() == "tia":
        return "Tia(" + match.group(
            3) + ") là phân giác của góc (" + match.group(1) + ")"
    else:
        return match.group(3) + " là phân giác của góc (" + match.group(
            1) + ")"


def tam_giac(match):
    return match.group(0).replace("tam", "Tam").replace("bằng", "=")


def doan_thang_co_gia_tri(match):
    return match.group(1) + " = " + match.group(2)


def goc_co_gia_tri(match):
    return "Góc(" + match.group(1) + ") = " + match.group(2)


def gia_tri(match):
    if match.group(1) == "góc":
        return "Góc(" + match.group(3).upper() + ")=" + match.group(4)
    elif match.group(2) is not None:
        return match.group(2) + " " + match.group(
            3).upper() + " = " + match.group(4)
    else:
        return match.group(3).upper() + " = " + match.group(4)


def hinh_dang(match):
    return match.group(0)


def getRuleFormat():
    listRule = []
    # 1. Điểm - điểm
    listRule.append((
        r"(?:điểm\s)?([A-Za-z](?:\,|và)?[A-Za-z]?(?:\,|và)?[A-Za-z]?)\s(nằm\sgiữa|thẳng\shàng|không\sthẳng\shàng)\s(?:với\snhau|hai\sđiểm\s([A-Za-z])\svà\s([A-Za-z]))",
        diem_diem))
    # 2. Điểm - đường
    listRule.append(
        (r"(?:điểm\s)?([A-Z])\s(thuộc|không\sthuộc)\sđường\sthẳng\s([A-Za-z])",
         diem_duong))
    # 3. Điểm - đoạn
    listRule.append((
        r"(?:điểm\s)?\s([A-Z])\s(nằm\sgiữa|không\snằm\sgiữa|thuộc|là\strung\sđiểm|là\sgiao\sđiểm)\s(?:(?:đoạn\sthẳng|của\shai\sđoạn\sthẳng|của)\s)([A-Za-z][A-Za-z])(?:\svà\s([A-Za-z][A-Za-z]))?",
        diem_doan))
    listRule.append((
        r"([A-Z])\svà\s([A-Z])\slần\slượt\s(nằm\sgiữa|không\snằm\sgiữa|thuộc|là\strung\sđiểm|là\sgiao\sđiểm)\s(?:(?:đoạn\sthẳng|của\shai\sđoạn\sthẳng|của)\s)([A-Za-z]{2})\svà\s([A-Za-z]{2})",
        diem_doan_extra))
    # 4. Điểm - tia
    listRule.append((
        r"điểm\s([A-Za-z])\s(thuộc\stia\s([A-Za-z][A-Za-z])|là\sgiao\sđiểm\scủa\s(tia|đoạn)\s([A-Za-z][A-Za-z])\svà\s(tia|đoạn)\s([A-Za-z][A-Za-z]))",
        diem_tia))
    # 5. Điểm - đường tròn
    listRule.append((
        r"điểm\s([A-Za-z])\s(thuộc|nằm\sngoài)\s(đường\s+tròn(?:\s+tâm)?\s+([A-Z])(?:(?:\s+bán\s+kính\s+)|\,)?([A-Z]))",
        diem_tron))
    # 6. Đoạn - đường tròn
    listRule.append((
        r"đoạn\s([A-Za-z][A-Za-z])\slà\s(tiếp\stuyến\scủa|dây\scung|đường\skính)\s(?:của\s)?(đường\s+tròn(?:\s+tâm)?\s+([A-Z])(?:(?:\s+bán\s+kính\s+)|\,)?([A-Z]))",
        doan_tron))
    # 7. Điểm - đoạn - đường tròn
    listRule.append((
        r"([A-Za-z])\slà\sgiao\sđiểm\scủa\s(đoạn\sthẳng\s([A-Za-z][A-Za-z])|đường\s+tròn(?:\s+tâm)?\s+([A-Z])(?:(?:\s+bán\s+kính\s+)|\,)?([A-Z]))\svà\s(đoạn\sthẳng\s([A-Za-z][A-Za-z])|đường\s+tròn(?:\s+tâm)?\s+([A-Z])(?:(?:\s+bán\s+kính\s+)|\,)?([A-Z]))",
        diem_doan_tron))
    # 8. Đoạn - Đoạn
    listRule.append((
        r"([A-Za-z][A-Za-z])\s(song\ssong|vuông|bằng|=)\s(?:với\s)?([A-Za-z][A-Za-z])",
        doan_doan))
    listRule.append((
        r"([A-Za-z])\slà\sgiao\sđiểm\scủa\sđoạn\s([A-Za-z][A-Za-z])\svà\s([A-Za-z][A-Za-z])",
        doan_giao_diem))
    # 9. Tia - Tia
    listRule.append((
        r"(tia\s([A-Za-z][A-Za-z]))\snằm\sgiữa\s(tia\s([A-Za-z][A-Za-z]))\svà\s(tia\s([A-Za-z][A-Za-z]))",
        tia_nam_giua))
    listRule.append((
        r"(tia\s([A-Za-z][A-Za-z]))\sđối(?:\snhau)?\s(tia\s([A-Za-z][A-Za-z]))",
        tia_doi_nhau))
    # 11-10 Điểm - Tia - Đoạn
    listRule.append((
        r"điểm\s([A-Z])\s(là\sgiao\sđiểm\scủa|nằm\sgiữa)\s(tia|đoạn)\s([A-Za-z][A-Za-z])\svà\s(tia|đoạn)\s([A-Za-z][A-Za-z])",
        diem_tia_doan))
    # 12. Đoạn - tam giác
    listRule.append((
        r"([A-Z][A-Z])\s+là\s+đường\s+cao\s+của\s+tam\s+giác(\svuông\scân\s|\svuông\s|\sđều\s|\scân\s|\s)([A-Z][A-Z][A-Z])",
        doan_tam_giac))
    # 13. Đoạn - tứ giác
    listRule.append((
        r"([A-Z][A-Z])\s+là\s+đường\s+cao\s+của\s+(hình\s+bình\s+hành|hình\s+thang)\s+([A-Z]{1,4})",
        doan_tu_giac))
    # 14. Góc - Góc

    listRule.append((
        r"góc\s([a-zA-Z][a-zA-Z][a-zA-Z])\s*(là|=|bằng)\s(góc\svuông|góc\s([a-zA-Z][a-zA-Z][a-zA-Z]))",
        goc_goc))

    # 15. Góc - Đoạn, Góc - Tia
    listRule.append((
        r"góc\s([a-zA-Z][a-zA-Z][a-zA-Z])\slà\sgóc\sphân\sgiác\scủa\s(tia|đoạn\sthẳng)\s([a-zA-Z][a-zA-Z])",
        goc_doan_tia))

    # 16 Tam giác
    listRule.append((
        r"(tam\sgiác)\s([A-Z][A-Z][A-Z])\s(bằng|=|đồng\sdạng)\stam\sgiác\s([A-Z][A-Z][A-Z])",
        tam_giac))
    # 2.2.3
    listRule.append((
        r"(góc\s)?((?:diện\stích|chu\svi|nửa\schu\svi)\s(?:tam\sgiác|tứ\sgiác))?\s*([A-Z]{2,4})\s*(?:=|bằng|có\s*độ\s*dài\s*là)\s*(\d+(\.\d+)?)",
        gia_tri))

    # 2.2.4
    listRule.append((
        r"(tam\sgiác|tứ\sgiác)\s([A-Z][A-Z][A-Z]([A-Z])?)\slà\s(tam\sgiác\s(cân|vuông|đều)|hình\sthang|hình\svuông|hình\stròn|hình\schữ\snhật|hình\sbình\shành|hình\sthoi)",
        hinh_dang))

    return listRule
