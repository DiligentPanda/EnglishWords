import configuration as config
from strategy import Strategy,RandomLinearStrategy
class Recorder:
    def __init__(self, words,strategy):
        self.words = words
        self.strategy = strategy

    def record(self, word, result):
        if result == config.CORRECT_KEY:
            word["correct"] += 1
            word["history"].append("c")
            self.strategy.counter["c"] += 1
            self.strategy.log["c"].append(word["spelling"])
        if result == config.WRONG_KEY:
            word["wrong"] += 1
            word["history"].append("w")
            self.strategy.counter["w"] += 1
            self.strategy.log["w"].append(word["spelling"])
        if result == config.NOTSURE_KEY:
            word["notSure"] += 1
            word["history"].append("n")
            self.strategy.counter["n"] += 1
            self.strategy.log["n"].append(word["spelling"])