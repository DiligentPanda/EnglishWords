

TYPE_INT=0
TYPE_STR=1
TYPE_LIST=2

headers_inFile=["英文单词","中文释义","list","unit","correct","notSure","wrong","history","发音文件","音标","comment"]
types_inFile=[   str,           str,      str,    str,     int,       int,       int,      str,      str,       str,     str]

headers=["spelling","answer","list","unit","correct","notSure","wrong","history","pronunciation","phoneticSymbol","comment"]
types=[TYPE_STR,TYPE_STR,TYPE_STR,TYPE_STR,TYPE_INT,TYPE_INT,TYPE_INT,TYPE_LIST,TYPE_STR,TYPE_STR,TYPE_STR]

dataPath="data/"
pronDataPath=dataPath+"pronunciation/"
logPath="log/"

CORRECT_KEY="a"
WRONG_KEY="s"
NOTSURE_KEY="d"


