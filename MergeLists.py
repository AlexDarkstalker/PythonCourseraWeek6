def merge(A, B):
    indA = 0
    indB = 0
    res = []
    while indA < len(A) and indB < len(B):
        if A[indA] > B[indB]:
            res.append(B[indB])
            indB += 1
        else:
            res.append(A[indA])
            indA += 1
    if indA == len(A):
        res.extend(B[indB:])
    if indB == len(B):
        res.extend(A[indA:])
    return res


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(*merge(list1, list2))
