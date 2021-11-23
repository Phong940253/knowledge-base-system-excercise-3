# -*- coding: utf-8 -*-
from WordSegmentation import WordSegmentation
import sys
if len(sys.argv) > 1:
    input = "".join(sys.argv[1:])
else:
    input = u"Cho tam giác ABC, vuông tại A, cạnh BC bằng 5cm, AC bằng 3cm. Tính diện tích tam giác ABC."
input = u"Cho tam giác ABC, vuông tại A, cạnh BC bằng 5cm, AC bằng 3cm. Tính diện tích tam giác ABC."
wordSegmentation = WordSegmentation(input)
wordSegmentation.process()
print(wordSegmentation.process().encode("utf-8"))
# print(wordSegmentation.hypothesisSentenceSegment,
#       wordSegmentation.goalSentenceSegment)

# wordSegmentation.transformToPreSL()
