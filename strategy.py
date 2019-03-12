import random

class Strategy:

    def __init__(self, words, filter=None):
        # to do: add a filter function object to select words by their attributes
        if filter:
            self.words = [word for word in words if filter(word) == True]
        else:
            self.words = words
        self.total = len(self.words)
        self.counter = {"c": 0, "n": 0, "w": 0}
        self.log = {"c": [], "n": [], "w": []}

    def randomChoice(self):
        return random.choice(self.words)

    def chooseWord(self):
        return self.randomChoice()

    def chooseWords(self):
        pass

    def stat(self):
        return "statistics:"

class RandomLinearStrategy(Strategy):

    def __init__(self, words, filter=None):
        Strategy.__init__(self,words,filter)
        self.indices=list(range(self.total))
        random.shuffle(self.indices)
        self.pointer = 0



    def chooseWord(self):
        if self.pointer>=len(self.indices):
            return None
        else:
            word =self.words[self.indices[self.pointer]]
            self.pointer+=1
            return word

    def stat(self):
        return "statistics:\ncorrect: %d, wrong: %d, not sure: %d, total:%d"%(self.counter["c"],self.counter["w"],self.counter["n"],self.total)