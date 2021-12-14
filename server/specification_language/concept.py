def formatConceptGoc(match):
    return match.group(1).capitalize() + "(" + match.group(2).upper() + ")"


def formatSecondUpper(match):
    return match.group(1) + " " + match.group(2).upper()


def formatTriangleWithAttributes(match):
    return match.group(1) + " " + match.group(2) + " " + match.group(3).upper()


def formatCircle(match):
    return "Đường tròn tâm " + match.group(1) + " bán kính " + match.group(2)


def formatLine(match):
    return "Đường thảng: " + match.group(1)


def getConcept():
    listConcept = []
    # listConcept.append(
    #     r"(?:bán|hái|gấp|mua|chở|trồng|đựng|)*\s*(?:được|có|dài|hết|về)+\s*(\d+)\s*((?:\w|\s)+)")
    listConcept.append((r"(TIA)\s+([A-Z]{2})", "\\g<1>(\\g<2>)"))
    listConcept.append((r"Đoạn\s+(?:thẳng\s+)?([A-Z]{2})", "\\g<1>"))
    listConcept.append((r"(?:Đường\sthẳng)\s+([a-z])", formatLine))
    listConcept.append((r"(góc)\s+([A-Z]{3})", formatConceptGoc))
    listConcept.append((r"(Tam giác)\s+([A-Z]{3})", formatSecondUpper))
    listConcept.append(
        (r"(Tam giác)\s+(vuông|cân|vuông\scân|đều)\s+([A-Z]{3})",
         formatTriangleWithAttributes))
    listConcept.append((r"(Hình\s+thang(?:\s+(?:cân|vuông))?)\s+([A-Z]{4})",
                        formatSecondUpper))
    listConcept.append(
        (r"(Hình\s+(?:bình\s+hành|thoi|vuông|chữ\s+nhật))\s+([A-Z]{4})",
         formatSecondUpper))
    listConcept.append((
        r"Đường\s+tròn(?:\s+tâm)?\s+([A-Z])(?:(?:\s+bán\s+kính\s+)|\,)?([A-Z])",
        formatCircle))
    return listConcept
