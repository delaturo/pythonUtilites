
from sort.sortAlgorithm import sortAlgorithm


class mergeSort(sortAlgorithm):

    def __init__(self):
        sortAlgorithm.__init__(self)

    def getDescription(self):
        return "Merge sort"

    def sortMethod(self, arr):
        if len(arr) > 1:
  
            half = len(arr)//2
    
            L = arr[:half]
            R = arr[half:]
    
            self.sortMethod(L)
            self.sortMethod(R)
    
            i = j = k = 0
            while i < len(L) and j < len(R):
                self.comparisons += 1
                if L[i] < R[j]:
                    arr[k] = L[i]
                    self.swaps += 1
                    i += 1
                else:
                    self.swaps += 1
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            while i < len(L):
                self.swaps += 1
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                self.swaps += 1
                arr[k] = R[j]
                j += 1
                k += 1

        return arr