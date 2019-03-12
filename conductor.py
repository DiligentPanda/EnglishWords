from words import Words
from audioManager import AudioManager
from strategy import Strategy,RandomLinearStrategy
from cmdUI import CmdUI
from recorder import Recorder
from PyQt5.QtCore import pyqtSignal,QObject,QCoreApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import QMediaPlayer
import sys
from sys import stdin
import configuration as config

class Conductor(QObject):

    finished = pyqtSignal()

    def __init__(self,wordFileName,filter=None):
        QObject.__init__(self)

        self.app = QCoreApplication(sys.argv)
        self.finished.connect(self.app.exit)
        self.words = Words(wordFileName)
        self.strategy = RandomLinearStrategy(self.words,filter)
        mp = QMediaPlayer()
        self.audioManager = AudioManager(mp)
        self.ui = CmdUI()
        self.recorder=Recorder(self.words,self.strategy)

        self.run()

    def log(self):
        import datetime
        now = datetime.datetime.now()
        fileName=now.strftime('%Y_%m_%d_%H_%M_%S')+"_log.txt"
        with open(config.logPath+fileName,"w") as f:
            f.write("Correct:\n")
            for word in self.strategy.log["c"]:
                f.write(word+"\n")
            f.write("\nWrong:\n")
            for word in self.strategy.log["w"]:
                f.write(word + "\n")
            f.write("\nNot sure:\n")
            for word in self.strategy.log["n"]:
                f.write(word + "\n")

    def run(self):

        self.ui.start()
        while 1:
            word = self.strategy.chooseWord()
            if word==None:
                print("This pass ends...")
                break

            self.ui.showWord(word)
            self.audioManager.prononce(word)
            instr = input()
            if instr == "q":
                break
            self.ui.showAnswer(word)

            result = input()
            while result not in [config.CORRECT_KEY,config.NOTSURE_KEY,config.WRONG_KEY,"q"]:
                result = input("invalid input...do it again...")
            if result == "q":
                break
            self.recorder.record(word,result)
        self.ui.showStatistics(self.strategy.stat())
        self.log()
        instr = input("Write to files?yes(y)/no(n):")
        while instr!='n' and  instr!='y':
            instr = input("Write to files?yes(y)/no(n):")
        if instr=='y':
            self.words.writeToFile()
        self.ui.end()

        self.finished.emit()

def listFilter(word,l):
    return word["list"] in l

def lastKUnknownFilter(word,k):
    return "n" in word["history"][-k:] or "w" in word["history"][-k:]

def filter(word,filters):
    for f in filters:
        if f(word)==False:
            return False
    return True

if __name__=="__main__":
    import functools
    import argparse
    parser = argparse.ArgumentParser(description="This is a description of (to do)...")
    parser.add_argument("-l",nargs="+")
    parser.add_argument("-k",nargs="?",const=1,type=int)
    flags=parser.parse_args(sys.argv[1:])
    l=flags.l
    k=flags.k
    myListFilter = functools.partial(listFilter,l=l)
    myFilters = [myListFilter]
    if k:
        myLastKUnknown = functools.partial(lastKUnknownFilter, k=k)
        myFilters.append(myLastKUnknown)
    myFilter = functools.partial(filter,filters=myFilters)
    conductor=Conductor(config.dataPath+"gre3000.xlsx",filter=myFilter)
