
from sort.sortAlgorithm import sortAlgorithm


class insertionSort(sortAlgorithm):

    def __init__(self):
        sortAlgorithm.__init__(self)

    def getDescription(self):
        return "Selection sort"

    def sortMethod(self, n):
        l = len(n)
        
        for i in range(l):

            k = n[i]

            j = i - 1
            while j >= 0  and k < n[j]:
                self.comparisons += 1
                n[j + 1] = n[j]
                self.swaps += 1
                j -= 1
            n[j+1] = k
            self.swaps += 1

        return n