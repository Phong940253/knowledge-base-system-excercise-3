from SentenceForm import SentenceForm


input = u"Cho tam giác ABC, vuông tại A, cạnh BC bằng 5cm, AC bằng 3cm. Tính diện tích tam giác ABC."
sentence = SentenceForm()
print(sentence.findSentenceForm(input))
# print(ViPosTagger.postagging(ViTokenizer.tokenize(input)))
