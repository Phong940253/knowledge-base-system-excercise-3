from SentenceForm import SentenceForm
import unidecode


class WordSegmentation:
    output = ""

    def __init__(self, input):
        self.input = input
        self.sentence = SentenceForm()
        self.sentenceSegment, self.sentencePos, self.preSLForm = self.sentence.findSentenceForm(
            input)
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

    def process(self):

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

        hypothsisPreSL = self.transformToPreSL(
            self.hypothesisSentenceSegment, self.hypothesisSentencePos, self.hypothesisPreSLForm)

        goalPreSL = self.transformToPreSL(
            self.goalSentenceSegment, self.goalSentencePos, self.goalPreSLForm)

        self.output += "to pre-SL sentence\nhypothesis\n"
        for i in hypothsisPreSL:
            self.output += i + "\n"
        self.output += "goal\n"
        for i in goalPreSL:
            self.output += i + "\n"

        self.output += "The result is processed in 'detail pre-SL to SL'\nbegin_exercise\nbegin_problem\n"
        self.output += self.input
        self.output += "\nbegin_hypothesis\nend_hypothesis"
        self.output += "\nbegin_goal\nend_goal"
        self.output += "\nend_problem\nend_exercise"
        return self.output

    def replacePreSLFormBySegment(self, segment, pos, preSLForm):
        return preSLForm.replace(pos, segment)

    def formatPreSL(self, PreSL):
        PreSL = PreSL.replace("_", "")
        PreSL = unidecode.unidecode(PreSL)
        PreSL = PreSL.upper()
        PreSL = PreSL.replace("CM", "cm")
        return PreSL

    def transformToPreSL(self, sentenceSegmentence, sentencePos, PreSLForm):
        PreSLs = []
        for i, v in enumerate(sentenceSegmentence):
            PreSL = PreSLForm[i]
            for j, char in enumerate(sentencePos[i].split("|")):
                # print(char, PreSL, v[j])
                PreSL = self.replacePreSLFormBySegment(v[j], char, PreSL)
            PreSLs.append(self.formatPreSL(PreSL))
        return PreSLs
