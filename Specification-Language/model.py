from WordSegmentation import WordSegmentation
import sys
if len(sys.argv) > 1:
    input = sys.argv[1]
else:
    input = u"Cho tam giác ABC, vuông tại A, cạnh BC bằng 5cm, AC bằng 3cm. Tính diện tích tam giác ABC."

wordSegmentation = WordSegmentation(input)
print(wordSegmentation.process())
# print(wordSegmentation.hypothesisSentenceSegment,
#       wordSegmentation.goalSentenceSegment)

# wordSegmentation.transformToPreSL()
