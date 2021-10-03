from sort.sortAlgorithm import sortAlgorithm


class recursiveBubleSort(sortAlgorithm):

    array = []

    def __init__(self, arr):
        sortAlgorithm.__init__(self)
        self.array = arr

    def getDescription(self):
        return "Buble sort.\nCompleijidad: O(n²)"

    def recursiveBuble(self, n = None):
        if not n:
            n = len(self.array)
        
        if n == 1:
            return
        
        for i in range(n - 1):
            self.comparisons += 1
            if self.array[i] > self.array[i + 1]:
                t = self.array[i]
                self.array[i] = self.array[i+1]
                self.array[i+1] = t
                self.swaps += 1
        
        self.recursiveBuble(n-1)

    def sortMethod(self, n):
        self.recursiveBuble()
        return self.array