import random


def CountSort(A):
    A[:] = QuickSort(A)


def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        R = []
        M = []
        for elem in A:
            if elem > q:
                R.append(elem)
            elif elem < q:
                L.append(elem)
            else:
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)


myList = list(map(int, input().split()))
CountSort(myList)
print(*myList)
