import configuration as config
from sys import stdout
class CmdUI:

    def __init__(self):
        pass

    def start(self):
        print("*** Help you to remember english words ***")
        print("Let's start!!!")
        print("Tips: to do...")

    def end(self):
        print("See you again \(-_-)/")
        print("***              THE END               ***")

    def pretty_print(self,s):
        '''
        this is specific to my own need
        '''
        print("*"*10)
        import re
        l=re.split(";|；",s)
        for m in l:
            print( "%s"%(m.strip()))
        print("*"*10)

    def showWord(self,word):
        self.pretty_print(word["spelling"])
        #stdout.write("Show answer?(you can push any key or q to quit)")
        #stdout.flush()

    def showAnswer(self,word):
        self.pretty_print(word["spelling"]+";"+"-"*10+";"+word["answer"])
        #stdout.write("correct(%s)/wrong(%s)/not sure(%s)/quit(q)"%(config.CORRECT_KEY,config.WRONG_KEY,config.NOTSURE_KEY))
        # stdout.flush()

    def showStatistics(self,stat):
        self.pretty_print(stat)