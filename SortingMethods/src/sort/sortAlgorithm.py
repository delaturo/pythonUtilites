
import time

class sortAlgorithm:

    initTime = 0
    endTime = 0
    swaps = 0
    comparisons = 0

    def __init__(self):
        self.initTime = 0
        self.endTime = 0
        self.swaps = 0
        self.comparisons = 0

    def sortMethod(self,n):
        return 0

    def sort(self, n):
        self.startTime()
        sn = self.sortMethod(n)
        st = self.stopTime()
        res = {
            'time' : st,
            'comparisons' : self.comparisons,
            'swaps': self.swaps,
            'arrayOrdered': sn
        }
        return res

    def getDescription(self):
        pass

    def startTime(self):
        self.startTime = time.time()

    def stopTime(self):
        self.endTime = time.time()
        return self.endTime - self.startTime 

