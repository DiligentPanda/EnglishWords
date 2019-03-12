from urllib import request, parse
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.Qt import QUrl
from PyQt5.QtCore import pyqtBoundSignal,QObject,pyqtSignal
import configuration as config

class AudioManager(QObject):
    playSignal = pyqtSignal()
    def __init__(self,mp):
        QObject.__init__(self,mp)
        self.mp = mp
        self.playSignal.connect(self.mp.play)

    def prononce(self,word):
        soundFile = word["pronunciation"]
        if soundFile == "notExist" or not self.check(soundFile):
            self.downloadSound(word)
        self.playAudio(word)

    def playAudio(self,word):
        self.mp.setMedia(QMediaContent(QUrl.fromLocalFile(word["pronunciation"])))
        self.playSignal.emit()

    def downloadSound(self,word):
        url = "http://dict.youdao.com/dictvoice"
        country = "2"#1-english,2-american
        params = {"audio": word["spelling"],"type":country}
        data = parse.urlencode(params).encode(encoding="utf-8")
        req = request.Request(url,data)
        with request.urlopen(req) as response:
            filePath = config.pronDataPath+word["spelling"]+"_yd.wav"
            with open(filePath,"wb") as f:
                f.write(response.read())
        word["pronunciation"] = filePath

    def check(self,fileName):
        # to do: check whether file is exist
        return True


if __name__=="__main__":
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtMultimedia import QMediaPlayer
    import sys
    app=QApplication(sys.argv)
    mp=QMediaPlayer()

    mp.setMedia(QMediaContent(QUrl.fromLocalFile(config.pronDataPath+"hello_yd.wav")))
    audioManager=AudioManager(mp)
    word={"spelling":"hello","pronunciation":"notExist"}
    audioManager.prononce(word)
    app.exec()
