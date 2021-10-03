import random
import sys
from sort.insertionSort import insertionSort
from sort.iterativeMergeSort import iterativeMergeSort
from sort.mergeSort import mergeSort
from sort.recursiveInsertionSort import recursiveInsertionSort

from sort.selectionSort import selectionSort
from sort.bubleSort import bubleSort
from sort.recursiveBubleSort import recursiveBubleSort

sys.setrecursionlimit(15000)

def generateNumbers(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(-100,100))
    return nums

n = 10000
print("Array generated...")

print("\n============= Selection sort =============")
arr = generateNumbers(n)
res = selectionSort().sort(arr)
print("Time: ", res['time'], "\nComparisons: ", res['comparisons'], "\nSwaps: ", res['swaps'])

print("\n============= Buble sort =============")
arr = generateNumbers(n)
res = bubleSort().sort(arr)
print("Time: ", res['time'], "\nComparisons: ", res['comparisons'], "\nSwaps: ", res['swaps'])

print("\n============= Recursive Buble sort =============")
arr = generateNumbers(n)
res = recursiveBubleSort(arr).sort(arr)
print("Time: ", res['time'], "\nComparisons: ", res['comparisons'], "\nSwaps: ", res['swaps'])

print("\n============= Insertion sort =============")
arr = generateNumbers(n)
res = insertionSort().sort(arr)
print("Time: ", res['time'], "\nComparisons: ", res['comparisons'], "\nSwaps: ", res['swaps'])

print("\n============= Recursive Insertion sort =============")
arr = generateNumbers(n)
res = recursiveInsertionSort().sort(arr)
print("Time: ", res['time'], "\nComparisons: ", res['comparisons'], "\nSwaps: ", res['swaps'])

print("\n============= Merge sort =============")
arr = generateNumbers(n)
res = mergeSort().sort(arr)
print("Time: ", res['time'], "\nComparisons: ", res['comparisons'], "\nSwaps: ", res['swaps'])

print("\n============= Iterative Merge sort =============")
arr = generateNumbers(n)
res = iterativeMergeSort().sort(arr)
print("Time: ", res['time'], "\nComparisons: ", res['comparisons'], "\nSwaps: ", res['swaps'])
