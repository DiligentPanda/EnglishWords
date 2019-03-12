import pandas as pd
import configuration as config
from word import Word
import tools

class WordsIO:
    def __init__(self,fileName):
        self.fileName=fileName

    def read(self):
        wordsList=[]
        return wordsList

    def write(self,wordsList):
        pass


class WordsIOFromExcel(WordsIO):
    def __init__(self,fileName):

        WordsIO.__init__(self,fileName)

    def read(self):
        wordList = []
        df = pd.read_excel(self.fileName,converters=dict([(config.headers_inFile[i],config.types_inFile[i]) for i in range(len(config.headers_inFile))]))
        df.fillna("",inplace=True)
        for index, row in df.iterrows():
            data = []
            for i in range(len(config.headers_inFile)):
                data.append(row[config.headers_inFile[i]])
                if config.types[i] == config.TYPE_INT:
                    data[i] = int(data[i])
                if config.types[i] == config.TYPE_LIST:
                    data[i] = tools.Tools.strToStrList(data[i])
            word = Word(data)
            wordList.append(word)
        del df
        return wordList

    def write(self,wordList):
        m = {}
        for i in range(len(config.headers_inFile)):
            if config.types[i]==config.TYPE_LIST:
                m[config.headers_inFile[i]] = [tools.Tools.strListToStr(word[config.headers[i]]) for word in wordList]
            else:
                m[config.headers_inFile[i]] = [word[config.headers[i]] for word in wordList]
        df = pd.DataFrame(m)

        with pd.ExcelWriter(self.fileName) as writer:
            df.to_excel(writer,columns=config.headers_inFile)

if __name__=="__main__":
    io=WordsIOFromExcel("data/test.xlsx")
    wordList=io.read()
    io.write(wordList)