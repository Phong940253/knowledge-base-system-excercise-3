from WordSegmentation import WordSegmentation

input = u"Cho tam giác ABC, vuông tại A, cạnh BC bằng 5cm, AC bằng 3cm. Tính diện tích tam giác ABC."
wordSegmentation = WordSegmentation(input)
print(wordSegmentation.process())
print(wordSegmentation.hypothesisSentenceSegment,
      wordSegmentation.goalSentenceSegment)
