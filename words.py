from word import Word
from wordsIO import WordsIOFromExcel

class Words:

    def __init__(self, fileName):
        self.wordList = []
        self.io = None
        self.fileName = fileName
        suffix = fileName.split(".")
        if suffix[-1] in ["xlsx","xls"]:
            self.io=WordsIOFromExcel(self.fileName)
        self.readFromFile()

    def readFromFile(self):
        self.wordList=self.io.read()

    def writeToFile(self):
        self.io.write(self.wordList)

    def __len__(self):
        return len(self.wordList)

    def __getitem__(self, index):
        return self.wordList[index]


