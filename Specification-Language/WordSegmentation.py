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

    def formatOutput(self, outputs):
        res = []
        for text in outputs:
            newText = text.replace("A", "tinhtu")
            newText = newText.replace("C", "Coordinating conjunction")
            newText = newText.replace("E", "thanhphan")
            newText = newText.replace("I", "thantu")
            newText = newText.replace("L", "Determiner")
            newText = newText.replace("M", "chuso")
            newText = newText.replace("N", "danhtuthuong")
            newText = newText.replace("Nc", "Noun Classifier")
            newText = newText.replace("Ny", "danhtuviettat")
            newText = newText.replace("Np", "danhturieng")
            newText = newText.replace("Nu", "danhtudonvi")
            newText = newText.replace("P", "daitu")
            newText = newText.replace("R", "trangtu")
            newText = newText.replace("S", "Subordinating conjunction")
            newText = newText.replace("T", "botu")
            newText = newText.replace("V", "dongtu")
            newText = newText.replace("X", "khongbiet")
            newText = newText.replace("F", "daucau")
            res.append(newText)
        return res

    def process(self):

        self.output = "Sentence segmentation and HG classification&#13;&#10;hypothesis&#13;&#10;"
        for i in self.formatOutput(self.hypothesisSentencePos):
            self.output += i + "&#13;&#10;"
        self.output += "goal&#13;&#10;"
        for i in self.formatOutput(self.goalSentencePos):
            self.output += i + "&#13;&#10;"
        self.output += "then transform to pre-SL form:&#13;&#10;hypothesis&#13;&#10;"
        for i in self.formatOutput(self.hypothesisPreSLForm):
            self.output += i + "&#13;&#10;"
        self.output += "goal&#13;&#10;"
        for i in self.formatOutput(self.goalPreSLForm):
            self.output += i + "&#13;&#10;"

        hypothsisPreSL = self.transformToPreSL(
            self.hypothesisSentenceSegment, self.hypothesisSentencePos, self.hypothesisPreSLForm)

        goalPreSL = self.transformToPreSL(
            self.goalSentenceSegment, self.goalSentencePos, self.goalPreSLForm)

        self.output += "to pre-SL sentence&#13;&#10;hypothesis&#13;&#10;"
        for i in hypothsisPreSL:
            self.output += i + "&#13;&#10;"
        self.output += "goal&#13;&#10;"
        for i in goalPreSL:
            self.output += i + "&#13;&#10;"

        self.output += "The result is processed in 'detail pre-SL to SL'&#13;&#10;begin_exercise&#13;&#10;begin_problem&#13;&#10;"
        self.output += unidecode.unidecode(self.input)
        self.output += "&#13;&#10;begin_hypothesis&#13;&#10;end_hypothesis"
        self.output += "&#13;&#10;begin_goal&#13;&#10;end_goal"
        self.output += "&#13;&#10;end_problem&#13;&#10;end_exercise"
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
