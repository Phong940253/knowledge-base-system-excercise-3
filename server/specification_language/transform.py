from .concept import getConcept
from .rule import getRuleFormat
import re


class Transform:
    exceptList = [r"(góc)\s+([A-Z]{3})"]
    exceptListNoInsensitive = [
        "gia_tri", "gia_tri_2", "diem_diem", "diem_doan"
    ]

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
                if condition[1].__name__ in self.exceptListNoInsensitive:
                    matches = re.finditer(condition[0], text,
                                          re.MULTILINE | re.UNICODE)
                    # print(matches)
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

    def transformAll(self, text):
        splitText = self.preProcess(text)

        print(splitText)
        result = []
        for text in splitText:
            result.append(self.transform(text).strip())
        return ";".join(result).replace(";", ";\n")
