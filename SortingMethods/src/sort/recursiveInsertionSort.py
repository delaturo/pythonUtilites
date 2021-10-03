from sort.sortAlgorithm import sortAlgorithm


class recursiveInsertionSort(sortAlgorithm):

    array = []

    def __init__(self):
        sortAlgorithm.__init__(self)

    def getDescription(self):
        return "Recursive Insertion Sort"

    def recursiveInsertion(self, n):
        if n<= 1:
            return
        
        self.recursiveInsertion(n-1)

        last = self.array[n-1]
        j = n - 2

        while (j >= 0 and self.array[j] > last):
            self.comparisons += 1
            self.array[j + 1] = self.array[j]
            self.swaps += 1
            j = j -1
        self.array[j + 1] = last
        self.swaps += 1

    def sortMethod(self, n):
        self.array = n
        self.recursiveInsertion(len(self.array))
        return self.array