from pyvi import ViTokenizer, ViPosTagger


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
            dictionary[key] = value
        return dictionary

    def __init__(self):
        self.object_definitions = self.readFile(
            "./data/sentence-form/object_attribute.txt", self.object_definitions)
        self.object_attributes = self.readFile(
            "./data/sentence-form/object_attribute.txt", self.object_attributes)
        self.object_relations = self.readFile(
            "./data/sentence-form/object_relations.txt", self.object_relations)
        self.object_properties = self.readFile(
            "./data/sentence-form/object_properties.txt", self.object_properties)
        self.object_functions = self.readFile(
            "./data/sentence-form/object_functions.txt", self.object_functions)

    def findSentenceForm(self, text):
        segment, pos = ViPosTagger.postagging(ViTokenizer.tokenize(text))
        combine = zip(segment, pos)
        for i in combine:
            pass