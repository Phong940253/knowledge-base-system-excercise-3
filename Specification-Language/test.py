from concept import getConcept
from rule import getRuleFormat
import re


class Transform:
    exceptList = [r"(góc)\s+([A-Z]{3})"]
    exceptListNoInsensitive = ["gia_tri_2", "gia_tri"]

    def __init__(self):
        self.listConcept = getConcept()
        self.listRule = getRuleFormat()

    def splitWord(self, text):
        listWord = []
        tempWord = []
        temp = text.split(".")
        for word in temp:
            tempWord += word.split(",")
        for word in tempWord:
            listWord += word.split(";")
        return listWord

    def preProcess(self, text):
        text = re.sub(r"(của)\s([A-Z]{2}), ([A-Z]{2})",
                      "\\g<1> \\g<2> và \\g<3>", text, 0,
                      re.MULTILINE | re.UNICODE)
        text = re.sub(r"\s([A-Z]), ([A-Z])\slần\slượt",
                      " \\g<1> và \\g<2> lần lượt", text, 0,
                      re.MULTILINE | re.UNICODE)

        # trường hợp có nhiều góc mà không có chữ "góc" thì thêm chữ "góc" vào trước các góc
        search = re.search(r"(góc)\s(?:([A-Z]{3}),\s)+([A-Z]{3})", text,
                           re.MULTILINE | re.UNICODE)
        if search is not None:
            original = search.group(0)
            tempText = original.replace("góc", "")

            result = re.sub(r"[^góc]([A-Z]{3})", " Góc(\\g<1>)", tempText, 0,
                            re.MULTILINE | re.UNICODE)
            result = result[1:]
            text = text.replace(original, result)

        # Xử lí trường hợp đều thuộc
        search = re.search(
            r"([C|c]ác\sđiểm\s)(?:[A-Z]\,?\s)+đều\sthuộc\s([A-Za-z])", text,
            re.MULTILINE | re.UNICODE)
        if search is not None:
            original = search.group(0)
            tempText = original.replace("đều thuộc", "thuộc")
            tempText = tempText.replace(search.group(1), "")

            result = re.sub(r"([A-Z])\,\s",
                            "\\g<1> thuộc " + search.group(2) + ";", tempText,
                            0, re.MULTILINE | re.UNICODE)
            text = text.replace(original, result)

        text = self.splitWord(text)
        return text

    def transformBy(self, text, conditions):
        for condition in conditions:
            if isinstance(condition[1],
                          str) or condition[0] in self.exceptList:
                # trường hợp chỉ thay thế đoạn text được chọn
                text = re.sub(condition[0], condition[1], text, 0,
                              re.MULTILINE | re.IGNORECASE | re.UNICODE)
            else:
                # trường hợp thay thế câu thành text trích xuất được
                if str(condition[1]) in self.exceptListNoInsensitive:
                    matches = re.finditer(condition[0], text,
                                          re.MULTILINE | re.UNICODE)
                else:
                    matches = re.finditer(
                        condition[0], text,
                        re.MULTILINE | re.IGNORECASE | re.UNICODE)
                for matchNum, match in enumerate(matches, start=1):
                    # print(condition[0], match)
                    text = condition[1](match)
        # print(text)
        return text

    def transform(self, text):
        # transform by rule
        text = self.transformBy(text, self.listRule)
        # transform by concept
        text = self.transformBy(text, self.listConcept)
        return text

    def solve(self, text):
        splitText = self.preProcess(text)

        print(splitText)
        result = []
        for text in splitText:
            result.append(self.transform(text).strip())
        return ";".join(result).replace(";", ";\n")


test1 = "Cho độ dài đoạn thẳng AB = 7cm, biết rằng C là trung điểm của AB. Tính đoạn AC và BC"
test2 = "Cho đoạn thẳng AB có độ dài là 4cm, điểm C nằm giữa hai điểm A và B. M, N lần lượt là trung điểm của AC, BC. Tính đoạn thẳng MN"
test3 = "Cho đoạn thẳng AK có độ dài là 9cm. Cho điểm B thuộc đoạn AK, C nằm giữa hai điểm A và B, biết rằng AC = 4cm, BC = 1cm. Tính đoạn AB và BK"
test4 = "Cho góc XOY = 110, biết rằng Tia OZ là tia phân giác của góc XOY, Tia OP là tia phân giác của góc ZOY, Tia Oz nằm giữa tia OP và Tia OX. Tính các góc ZOY, ZOX, POZ, POX, POY."
test5 = "Cho điểm M thuộc tia OX, Và N thuộc Tia OY, K thuộc tia OX, biết rằng OM + ON = OK, OM = 4cm; ON = 6cm. Tính đoạn MN, OK, MK, NK."
test6 = "Cho đoạn thẳng AB, biết rằng AB = 11cm, M nằm giữa hai điểm A và B, có MB - MA = 5cm. Tính đoạn MA, MB."
test7 = "Cho OI và Tia OK đối nhau. I là giao điểm của Tia IO và đoạn AB, biết rằng góc KOA = 120 (độ), góc BOI = 45 (độ), Tia OA nằm giữa Tia OK và Tia OI, Tia OB nằm giữa Tia OK và Tia OI. Tính các góc KOB, AOI và BOA."
# TODO

test8 = "Cho đường thẳng d, các điểm A, B, C, K đều thuộc d, biết rằng K nằm giữa điểm A và C, C nằm giữa điểm K và B. Điểm O bất kì không thuộc d sao cho góc AOK = 30 (độ), KOC = 40 (độ), AOB = 90 (độ). Tính các góc AOC, COB, KOB"

engine = Transform()
# print("Câu 1:\n" + engine.solve(test1) + "\n")
# print("Câu 2:\n" + engine.solve(test2) + "\n")
# print("Câu 3:\n" + engine.solve(test3) + "\n")
print("Câu 4:\n" + engine.solve(test4) + "\n")
# print("Câu 5:\n" + engine.solve(test5) + "\n")
# print("Câu 6:\n" + engine.solve(test6) + "\n")
# print("Câu 7:\n" + engine.solve(test7) + "\n")
# print("Câu 8:\n" + engine.solve(test8) + "\n")