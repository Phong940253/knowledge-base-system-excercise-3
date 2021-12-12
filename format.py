import re
from typing import Text
# 2.2.1. Cú pháp câu viết cho giả thiết là một khái niệm
def tamGiac(text):
    regex = r"tam\sgiác(\svuông\scân\s|\svuông\s|\scân\s|\sđều\s|\s)([A-Za-z][A-Za-z][A-Za-z])\s?(vuông\svà\scân\stại|vuông\stại|cân\stại)?\s?([A-Z])?"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        reName=match.group(2)
        if match.group(1).casefold() in [" vuông "," cân "," vuông cân "]:
            reName=match.group(4)
            for name in match.group(2):
                if name.casefold()!= match.group(4).casefold():
                    reName = reName+name
        DS.append("Tam giác"+match.group(1)+reName)
    return DS
def tuGiac(text):
    regex = r"(tứ\sgiác|hình\sthang(\scân|\svuông)?|hình\sbình\shành|hình\sthoi|hình\svuông|hình\schữ\snhật)\s([A-Za-z][A-Za-z][A-Za-z][A-Za-z])"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append(match.group(1).capitalize()+" "+match.group(3))
    return DS
def duongTron(text):
    regex = r"Đường\s+tròn(?:\s+tâm)?\s+([A-Z])(?:(?:\s+bán\s+kính\s+)|\,)?([A-Z])"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)

def tia_goc_doan_duongThang(text):
    regex = r"(tia|đoạn\sthẳng|đường\sthẳng|góc)\s([A-Za-z][A-Za-z]?[A-Za-z]?)"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append("Đường tròn tâm " + match.group(1) + " bán kính " + match.group(2))
    return DS
    DS = []
    for match in matches:
        if match.group(1).casefold()=="tia":
            DS.append("Tia("+match.group(2)+")")
        elif match.group(1).casefold()=="đoạn thẳng":
            DS.append(match.group(2))
        elif match.group(1).casefold()=="đường thẳng":
            DS.append("Đường thẳng: "+match.group(2))
        elif match.group(1).casefold()=="góc":
            DS.append("Góc("+match.group(2)+")")
    return DS
# 1. Điểm - điểm
def diem_diem(text):
    regex=r"(?:điểm\s)?([A-Za-z](?:\,|và)?[A-Za-z]?(?:\,|và)?[A-Za-z]?)\s(nằm\sgiữa|thẳng\shàng|không\sthẳng\shàng)\s(với\snhau|hai\sđiểm\s([A-Za-z])\svà\s([A-Za-z]))"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        if match.group(2).casefold()=="nằm giữa":
            DS.append(match.group(1)+" "+match.group(2)+" "+match.group(4)+","+match.group(5))
        else:
            DS.append(match.group(1)+" "+match.group(2))
    return DS
# 2. Điểm - đường thẳng
def diem_duong(text):
    regex = r"(?:điểm\s)?([A-Z])\s(thuộc|không\sthuộc)\sđường\sthẳng\s([A-Za-z])"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append(match.group(1)+" "+ match.group(2)+" "+match.group(3))
    return DS
# 3. Điểm - đoạn
def diem_doan(text):
    regex = r"(?:điểm\s)?([A-Z])\s(nằm\sgiữa|không\snằm\sgiữa|thuộc|là\strung\sđiểm|là\sgiao\sđiểm)\s(?:đoạn\sthẳng|của\shai\sđoạn\sthẳng)\s([A-Za-z][A-Za-z])(\svà\s([A-Za-z][A-Za-z]))?"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        if match.group(2).casefold()=="là giao điểm":
            DS.append(match.group(1)+" "+match.group(2)+" của "+match.group(3)+" và "+match.group(5))
        elif match.group(2).casefold()=="là trung điểm":
            DS.append(match.group(1)+" "+match.group(2)+" của "+match.group(3))
        else:
            DS.append(match.group(1)+" "+match.group(2)+" "+match.group(3))
    return DS
# 4. Điểm - tia
def diem_tia(text):
    regex = r"điểm\s([A-Za-z])\s(thuộc\stia\s([A-Za-z][A-Za-z])|là\sgiao\sđiểm\scủa\s(tia|đoạn)\s([A-Za-z][A-Za-z])\svà\s(tia|đoạn)\s([A-Za-z][A-Za-z]))"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        if "thuộc" in match.group(2).casefold():
            DS.append(match.group(1)+" thuộc Tia("+match.group(3)+")")
        else:
            DS.append(match.group(1)+" là giao điểm của "+match.group(4)+"("+match.group(5)+") và "+match.group(6)+"("+match.group(7)+")")
    return DS
# 5. Điểm - đường tròn
def diem_tron(text):
    regex = r"điểm\s([A-Za-z])\s(thuộc|nằm\sngoài)\s(đường\s+tròn(?:\s+tâm)?\s+([A-Z])(?:(?:\s+bán\s+kính\s+)|\,)?([A-Z]))"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append(match.group(1)+" "+match.group(2)+" đường tròn tâm "+match.group(4)+" bán kính "+match.group(5))
    return DS
# 6. Đoạn - đường tròn
def doan_tron(text):
    regex = r"đoạn\s([A-Za-z][A-Za-z])\slà\s(tiếp\stuyến\scủa|dây\scung|đường\skính)\s(?:của\s)?(đường\s+tròn(?:\s+tâm)?\s+([A-Z])(?:(?:\s+bán\s+kính\s+)|\,)?([A-Z]))"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append(match.group(1)+" là "+match.group(2)+" đường tròn tâm "+match.group(4)+" bán kính "+match.group(5))
    return DS

# 7. Điểm - đoạn - đường tròn
def diem_doan_tron(text):
    regex = r"([A-Za-z])\slà\sgiao\sđiểm\scủa\s(đoạn\sthẳng\s([A-Za-z][A-Za-z])|đường\s+tròn(?:\s+tâm)?\s+([A-Z])(?:(?:\s+bán\s+kính\s+)|\,)?([A-Z]))\svà\s(đoạn\sthẳng\s([A-Za-z][A-Za-z])|đường\s+tròn(?:\s+tâm)?\s+([A-Z])(?:(?:\s+bán\s+kính\s+)|\,)?([A-Z]))"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        if "đoạn thẳng" in match.group(2).casefold():
            DS.append(match.group(1)+" là giao điểm của "+match.group(3)+" và đường tròn tâm"+match.group(8)+" bán kính "+match.group(9))
        else:
            DS.append(match.group(1)+" là giao điểm của "+match.group(7)+" và đường tròn tâm"+match.group(4)+" bán kính "+match.group(5))
    return DS

# 8. Đoạn - Đoạn

def doan_doan(text):
    regex = r"([A-Za-z][A-Za-z])\s(song\ssong|vuông|bằng|=)\s(?:với\s)?([A-Za-z][A-Za-z])"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        if match.group(2).casefold() == "vuông":
            DS.append(match.group(1)+" vuông góc "+match.group(3))
        elif match.group(2).casefold() == "bằng":
            DS.append(match.group(1)+" = "+match.group(3))
        else:
            DS.append(match.group(0))
    return DS
def doan_giao_diem(text):
    regex = r"([A-Za-z])\slà\sgiao\sđiểm\scủa\sđoạn\s([A-Za-z][A-Za-z])\svà\s([A-Za-z][A-Za-z])"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append(match.group(1)+" là giao điểm của "+match.group(2)+" và "+match.group(3))
    return DS
# 9. Tia - Tia


def tia_nam_giua(text):
    regex = r"(tia\s([A-Za-z][A-Za-z]))\snằm\sgiữa\s(tia\s([A-Za-z][A-Za-z]))\svà\s(tia\s([A-Za-z][A-Za-z]))"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append("Tia("+match.group(2)+") nằm giữa Tia(" +
                  match.group(4)+"),Tia("+match.group(6)+")")
    return DS


def tia_doi_nhau(text):
    regex = r"(tia\s([A-Za-z][A-Za-z]))\sđối(?:\snhau)?\s(tia\s([A-Za-z][A-Za-z]))"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append("Tia("+match.group(2)+") đối Tia("+match.group(4)+")")
    return DS


# 11-10 Điểm - Tia - Đoạn
def diem_tia_doan(text):
    regex = r"điểm\s([A-Z])\s(là\sgiao\sđiểm\scủa|nằm\sgiữa)\s(tia|đoạn)\s([A-Za-z][A-Za-z])\svà\s(tia|đoạn)\s([A-Za-z][A-Za-z])"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append("Điểm " + match.group(1)+" "+match.group(2)+" "+match.group(3) +
                  "("+match.group(4)+") và "+match.group(5)+"("+match.group(6)+")")
    return DS
# 12. Đoạn - tam giác


def doan_tam_giac(text):
    regex = r"([A-Z][A-Z])\s+là\s+đường\s+cao\s+của\s+tam\s+giác(\svuông\scân\s|\svuông\s|\sđều\s|\scân\s|\s)([A-Z][A-Z][A-Z])"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append(match.group(0))
    return DS
# 13. Đoạn - tứ giác


def doan_tu_giac(text):
    regex = r"([A-Z][A-Z])\s+là\s+đường\s+cao\s+của\s+(hình\s+bình\s+hành|hình\s+thang)\s+([A-Z]{1,4})"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append(match.group(0))
    return DS

# 14. Góc - Góc


def goc_goc(text):
    regex = r"góc\s([a-zA-Z][a-zA-Z][a-zA-Z])\s*(là|=|bằng)\s(góc\svuông|góc\s([a-zA-Z][a-zA-Z][a-zA-Z]))"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        if match.group(2) in ["=", "bằng"]:
            DS.append("Góc("+match.group(1)+") = góc("+match.group(4)+")")
        else:
            DS.append("Góc("+match.group(1)+") là góc vuông")
    return DS

# 15. Góc - Đoạn, Góc - Tia


def goc_doan_tia(text):
    regex = r"góc\s([a-zA-Z][a-zA-Z][a-zA-Z])\slà\sgóc\sphân\sgiác\scủa\s(tia|đoạn\sthẳng)\s([a-zA-Z][a-zA-Z])"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        if match.group(2).casefold() == "tia":
            DS.append(
                "Tia("+match.group(3)+") là phân giác của góc ("+match.group(1)+")")
        else:
            DS.append(match.group(3) +
                      " là phân giác của góc ("+match.group(1)+")")

    return DS

# 16 Tam giác


def tam_giac(text):
    regex = r"(tam\sgiác)\s([A-Z][A-Z][A-Z])\s(bằng|=|đồng\sdạng)\stam\sgiác\s([A-Z][A-Z][A-Z])"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append(match.group(0).replace("tam", "Tam").replace("bằng", "="))
    return DS
# 2.2.3


def doan_thang_co_gia_tri(text):
    regex = r"đoạn?.*([A-Z][A-Z])\s*(?:=|bằng|có\s*độ\s*dài\s*là)?\s*(\d+(\.\d+)?)"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append(match.group(1)+" = " + match.group(2))
    return DS


def goc_co_gia_tri(text):
    regex = r"(?:góc|\,)\s*([A-Z][A-Z][A-Z])\s*(?:=|bằng)+\s*(\d{1,3})"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append("Góc("+match.group(1)+") = " + match.group(2))
    return DS

# Chu vi diện tích
def DT_CV_NCV(text):
    regex = r"(diện\stích|chu\svi|nửa\schu\svi)\s(tam\sgiác|tứ\sgiác)\s+([A-Z][A-Z][A-Z]([A-Z])?)\s+(?:=|bằng|là)\s+(\d+(\.\d+)?)"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append(match.group(1)+" " + match.group(2)+" " +
                  match.group(3)+" = " + match.group(5))
    return DS

# 2.2.4


def hinh_dang(text):
    regex = r"(tam\sgiác|tứ\sgiác)\s([A-Z][A-Z][A-Z]([A-Z])?)\slà\s(tam\sgiác\s(cân|vuông|đều)|hình\sthang|hình\svuông|hình\stròn|hình\schữ\snhật|hình\sbình\shành|hình\sthoi)"
    matches = re.finditer(regex, text, re.MULTILINE | re.IGNORECASE)
    DS = []
    for match in matches:
        DS.append(match.group(0))
    return DS

# DÙNG ĐỂ TEST

# test_goc = "Cho giá trị của một góc:góc ABC = 90, BCD=90"
# test_dien_tich_tam_giac = "Cho giá trị diện tích của một tam giác: chu vi tứ giác ABCD = 12 (cm)"
# test_doan_thang = "Cho đoạn AB = 5cm, AM = 3.7, MB = 2.3. Chứng minh rằng:M không nằm giữa đoạn AB,B không nằm giữa AM và MAB không thẳng hàng."
# test_hinh_dang = "Tam giác là tam giác Cân:Tam giác ABC là tam giác cân Tam giác ABC là tam giác vuông Tam giác ABC là tam giác đều Tứ giác ABCD là hình thang Tứ giác ABCD là hình bình hành"
# test_tam_giac = "Hai tam giác bằng nhau tam giác ABC bằng tam giác EDF tam giác ABC đồng dạng tam giác EDF"
# test_goc_doan_tia = "Đoạn phân giác của một góc: góc ABC là góc phân giác của đoạn thẳng BE góc xOy là góc phân giác của tia Oz"
# test_goc_goc = "góc ABC = góc EFG góc xOy là góc vuông"
# test_doan_tu_giac = "AH là đường cao của hình thang ABCD AH là đường cao của hình bình hành ABCD"
# test_doan_tam_giac = "AH là đường cao của tam giác ABC AH là đường cao của tam giác vuông ABC AH là đường cao của tam giác cân ABC AH là đường cao của tam giác vuông cân ABC AH là đường cao của tam giác đều ABC"
# test_diem_tia_doan = "điểm M là giao điểm của tia Ox và đoạn AB"
# test_tia_nam_giua = "tia Oz nằm giữa tia Ox và tia Oy"
# test_tia_doi_nhau = "Tia Oz đối Tia Oy"
# test_doan_doan="AB song song CD AB vuông với CD AB bằng CD"
# test_tam_giac="tam giác ABC tam giác vuông ABC vuông tại B tam giác cân ABC cân tại B tam giác vuông cân ABC vuông và cân tại B tam giác đều ABC"
# test_tu_giac="tứ giác ABCD hình thang ABCD hình thang cân ABCD hình thang vuông ABCD hình bình hành ABCD hình thoi ABCD hình vuông ABCD hình chữ nhật ABCD"
# DS = tuGiac(test_tu_giac)
# for match in DS:
#     print(match)
