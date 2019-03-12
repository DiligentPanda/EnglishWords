class Tools:
    splitChar='#'

    def strListToStr(l):
        return Tools.splitChar.join(l)

    def strToStrList(s):
        if len(s)==0:
            return []
        else:
            return s.split(Tools.splitChar)

if __name__=="__main__":
    s=""
    l = Tools.strToStrList(s)
    s = Tools.strListToStr(l)

    print(s)
    print(l)