from concept import getConcept
from rule import getRuleFormat
import re


class Transform:
    def __init__(self, str):
        self.listConcept = getConcept()
        self.listRule = getRuleFormat()
        self.str = str

    def splitWord(self, text):
        listWord = []
        temp = text.split(",")
        for word in temp:
            listWord += word.split(".")
        return listWord

    def preProcess(self):
        self.str = self.splitWord(self.str)

    def transformBy(self, text, conditions):
        for condition in conditions:
            if isinstance(condition[1], str):
                # trường hợp chỉ thay thế đoạn text được chọn
                text = re.sub(condition[0], condition[1], text,
                              re.MULTILINE | re.IGNORECASE)
            else:
                # trường hợp thay thế câu thành text trích xuất được
                matches = re.finditer(condition[0], text,
                                      re.MULTILINE | re.IGNORECASE)
                for matchNum, match in enumerate(matches, start=1):
                    text = condition[1](match)
        # print(text)
        return text

    def transform(self, text):
        # transform by rule
        text = self.transformBy(text, self.listRule)
        # transform by concept
        text = self.transformBy(text, self.listConcept)
        return text

    def solve(self):
        self.preProcess()
        # print(self.str)
        result = []
        for text in self.str:
            result.append(self.transform(text).strip())
        return ";\n".join(result)


test_str = "Cho độ dài đoạn thẳng AB = 7cm, biết rằng C là trung điểm của AB. Tính đoạn AC và BC"

engine = Transform(test_str)
print(engine.solve())
