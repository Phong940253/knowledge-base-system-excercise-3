from SentenceForm import SentenceForm


class WordSegmentation:
    output = ""

    def __init__(self, input):
        self.sentence = SentenceForm()
        self.sentenceSegment, self.sentencePos, self.preSLForm = self.sentence.findSentenceForm(
            input)

    def process(self):
        self.hypothesisSentenceSegment = []
        self.hypothesisSentencePos = []
        self.hypothesisPreSLForm = []

        self.goalSentenceSegment = []
        self.goalSentencePos = []
        self.goalPreSLForm = []
        for i, v in enumerate(self.sentencePos):
            if v[0] == "V":
                self.goalSentenceSegment.append(self.sentenceSegment[i])
                self.goalSentencePos.append(v)
                self.goalPreSLForm.append(self.preSLForm[i])
            else:
                self.hypothesisSentenceSegment.append(self.sentenceSegment[i])
                self.hypothesisSentencePos.append(v)
                self.hypothesisPreSLForm.append(self.preSLForm[i])

        self.output = "sentence segmentation and HG classification\nhypothesis\n"
        for i in self.hypothesisSentencePos:
            self.output += i + "\n"
        self.output += "goal\n"
        for i in self.goalSentencePos:
            self.output += i + "\n"
        self.output += "then transform to pre-SL form:\nhypothesis\n"
        for i in self.hypothesisPreSLForm:
            self.output += i + "\n"
        self.output += "goal\n"
        for i in self.goalPreSLForm:
            self.output += i + "\n"
        return self.output

# print(ViPosTagger.postagging(ViTokenizer.tokenize(input)))
