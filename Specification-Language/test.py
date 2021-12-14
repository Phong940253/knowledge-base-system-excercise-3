from concept import getConcept
from rule import getRuleFormat
import re


class Transform:
    def __init__(self):
        self.listConcept = getConcept()
        self.listRule = getRuleFormat()

    def splitWord(self, text):
        listWord = []
        temp = text.split(".")
        for word in temp:
            listWord += word.split(",")
        return listWord

    def preProcess(self, text):
        text = re.sub(r"\s([A-Z]{2}), ([A-Z]{2})", "\\g<1> và \\g<2>", text, 0,
                      re.MULTILINE | re.IGNORECASE | re.UNICODE)
        text = re.sub(r"\s([A-Z]), ([A-Z])", "\\g<1> và \\g<2>", text, 0,
                      re.MULTILINE | re.IGNORECASE | re.UNICODE)
        text = self.splitWord(text)
        return text

    def transformBy(self, text, conditions):
        for condition in conditions:
            if isinstance(condition[1], str):
                # trường hợp chỉ thay thế đoạn text được chọn
                text = re.sub(condition[0], condition[1], text, 0,
                              re.MULTILINE | re.IGNORECASE | re.UNICODE)
            else:
                # trường hợp thay thế câu thành text trích xuất được
                matches = re.finditer(
                    condition[0], text,
                    re.MULTILINE | re.IGNORECASE | re.UNICODE)
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

    def solve(self, text):
        splitText = self.preProcess(text)
        result = []
        for text in splitText:
            result.append(self.transform(text).strip())
        return ";\n".join(result)


test1 = "Cho độ dài đoạn thẳng AB = 7cm, biết rằng C là trung điểm của AB. Tính đoạn AC và BC"
test2 = "Cho đoạn thẳng AB có độ dài là 4cm, điểm C nằm giữa hai điểm A và B. M, N lần lượt là trung điểm của AC, BC. Tính đoạn thẳng MN."

engine = Transform()
print(engine.solve(test1))
print(engine.solve(test2))
