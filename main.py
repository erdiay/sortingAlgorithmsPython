from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort

def bubbleSortTest():
    A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    bubbleSort(A)
    print("Sorted array: ")
    print()
    for i in A:
        print(i, end=" ") 

def selectionSortTest():
    A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    selectionSort(A)
    print("Sorted array: ")
    print()
    for i in A:
        print(i, end=" ") 

def insertionSortTest():
    A = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    insertionSort(A)
    print("Sorted array: ")
    print()
    for i in A:
        print(i, end=" ") 

#bubbleSortTest()
#selectionSortTest()
insertionSortTest()