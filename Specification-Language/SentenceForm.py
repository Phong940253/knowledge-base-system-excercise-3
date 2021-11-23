import re
from pyvi import ViTokenizer, ViPosTagger
import numpy as np


class SentenceForm:
    object_definitions = {}
    object_attributes = {}
    object_relations = {}
    object_properties = {}
    object_functions = {}

    def readFile(self, file, dictionary):
        f = open(file)
        for line in f:
            key, value = line.split(":")
            dictionary[key] = value.rstrip("\n")
        return dictionary

    def __init__(self):
        self.object_definitions = self.readFile(
            "../../Specification-Language/data/sentence-form/object_definition.txt", self.object_definitions)
        self.object_attributes = self.readFile(
            "../../Specification-Language/data/sentence-form/object_attribute.txt", self.object_attributes)
        # self.object_relations = self.readFile(
        #     "./data/sentence-form/object_relations.txt", self.object_relations)
        # self.object_properties = self.readFile(
        #     "./data/sentence-form/object_properties.txt", self.object_properties)
        # self.object_functions = self.readFile(
        #     "./data/sentence-form/object_functions.txt", self.object_functions)

    def splitArrayByValue(self, array1, array2, value):
        result1 = []
        result2 = []
        temp1 = []
        temp2 = []
        for i in range(len(array2)):
            if array2[i] == value:
                if len(temp1) > 0:
                    result1.append(temp1)
                    result2.append(temp2)
                    temp1 = []
                    temp2 = []
            else:
                temp1.append(array1[i])
                temp2.append(array2[i])
        if len(temp1) > 0:
            result1.append(temp1)
            result2.append(temp2)

        return result1, result2

    def createSenctenceForm(self, text):
        segment, pos = ViPosTagger.postagging(ViTokenizer.tokenize(text))
        # combine = zip(segment, pos)
        # Tách mảng tại các phần tử "F"
        splitSegment, splitPos = self.splitArrayByValue(segment, pos, "F")

        # chuẩn hóa chuỗi pos
        newsplitPos = []
        for pos in splitPos:
            newPos = []
            for idx, val in enumerate(pos):
                num = pos[:idx].count(val)
                newPos.append(val + str(num + 1))
            newsplitPos.append(newPos)

        return splitSegment, newsplitPos

    def getPreSLForm(self, key):
        if key in self.object_definitions:
            return self.object_definitions[key]
        if key in self.object_attributes:
            return self.object_attributes[key]
        if key in self.object_relations:
            return self.object_relations[key]
        if key in self.object_properties:
            return self.object_properties[key]
        if key in self.object_functions:
            return self.object_functions[key]
        return False

    def findSentenceForm(self, text):
        segments, poss = self.createSenctenceForm(text)
        sentenceSegment = []
        sentencePos = []
        preSLForm = []
        for idx, pos in enumerate(poss):

            checki = []
            checkj = []
            # lưu các chỉ số tránh trường hợp trùng mẫu câu

            for i in range(len(pos)):
                for j in range(i + 1, len(pos) + 1):
                    form = "|".join(pos[i:j])
                    if self.getPreSLForm(form) and i not in checki and j not in checkj:
                        checki.append(i)
                        checkj.append(j)
                        sentenceSegment.append(segments[idx][i:j])
                        sentencePos.append(form)
                        preSLForm.append(self.getPreSLForm(form))
                        break
        return sentenceSegment, sentencePos, preSLForm
