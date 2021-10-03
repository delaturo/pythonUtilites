
from sort.sortAlgorithm import sortAlgorithm


class iterativeMergeSort(sortAlgorithm):

    def __init__(self):
        sortAlgorithm.__init__(self)

    def getDescription(self):
        return "Merge sort"

    def merge(self, left, right):
        if not len(left) or not len(right):
            return left or right
    
        result = []
        i, j = 0, 0
        while (len(result) < len(left) + len(right)):
            self.comparisons += 1
            if left[i] < right[j]:
                result.append(left[i])
                self.swaps += 1
                i+= 1
            else:
                result.append(right[j])
                self.swaps += 1
                j+= 1
            if i == len(left) or j == len(right):
                result.extend(left[i:] or right[j:])
                self.swaps += 1
                break
    
        return result

    def sortMethod(self, arr):
        if len(arr) < 2:
            return arr
    
        middle = len(arr)//2
        left = self.sortMethod(arr[:middle])
        right = self.sortMethod(arr[middle:])
    
        return self.merge(left, right)