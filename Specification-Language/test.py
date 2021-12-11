
import re


def test(match):
    return match.group(1) + " " + match.group(2) + " " + match.group(3).upper()
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility


def formatSecondUpper(match):
    return "Đường tròn tâm " + match.group(1) + " bán kính " + match.group(2)


regex = r"Đường\s+tròn(?:\s+tâm)?\s+([A-Z])(?:(?:\s+bán\s+kính\s+)|\,)?([A-Z])"

test_str = "Đường tròn tâm O bán kính R Đường tròn tâm O,R hoặc Đường tròn O,R Đường tròn O bán kính R"

matches = re.finditer(regex, test_str, re.MULTILINE | re.IGNORECASE)

for matchNum, match in enumerate(matches, start=1):
    print(match)
    print(formatSecondUpper(match))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
