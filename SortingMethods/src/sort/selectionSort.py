
from sort.sortAlgorithm import sortAlgorithm


class selectionSort(sortAlgorithm):

    def __init__(self):
        sortAlgorithm.__init__(self)

    def getDescription(self):
        return "Selection sort"

    def sortMethod(self, n):
        l = len(n)
        for i in range(l):
            minI = i
            for j in range(i+1, l):
                self.comparisons += 1
                if n[minI] > n[j]:
                    minI = j
            t = n[i]
            n[i] = n[minI]
            n[minI] = t
            self.swaps += 1
        return n