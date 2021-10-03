
from sort.sortAlgorithm import sortAlgorithm


class bubleSort(sortAlgorithm):

    def __init__(self):
        sortAlgorithm.__init__(self)

    def getDescription(self):
        return "Buble sort.\nCompleijidad: O(n²)"

    def sortMethod(self, n):
        l = len(n)
        for i in range(l):
            for j in range (0, l-i-1):
                self.comparisons += 1
                if n[j] > n[j+1]:
                    t = n[j]
                    n[j] = n[j+1]
                    n[j+1] = t
                    self.swaps += 1
        return n