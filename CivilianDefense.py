def sortDist(villageNum):
    return villageNum[1]


numVil = int(input())
villageList = list(map(int, input().split()))
numShelter = int(input())
shelterList = list(map(int, input().split()))
villageListNum = []
shelterListNum = []
for i in range(1, len(villageList) + 1):
    villageListNum.append((i, villageList[i - 1]))
for i in range(1, len(shelterList) + 1):
    shelterListNum.append((i, shelterList[i - 1]))

villageListNum.sort(key=sortDist)
shelterListNum.sort(key=sortDist)
# print(*villageList)
# print(*shelterList)
# print(*villageListNum)
# print(*shelterListNum)
result = []
curShelterIndex = 0
for i in range(len(villageListNum)):
    if not len(result):
        if villageListNum[0][1] <= shelterListNum[0][1]:
            for _ in range(len(villageListNum)):
                result.append(0)
            result[villageListNum[0][0] - 1] = shelterListNum[0][0]
        elif villageListNum[0][1] >= shelterListNum[-1][1]:
            for _ in range(len(villageListNum)):
                result.append(0)
            result[villageListNum[0][0] - 1] = \
                shelterListNum[-1][0]
            curShelterIndex = len(shelterListNum) - 1
        else:
            minDist = 10**10
            curDist = abs(villageListNum[0][1] - shelterListNum[0][1])
            numElem = 1
            j = 1
            while curDist < minDist and j < len(shelterListNum):
                minDist = curDist
                curDist = abs(villageListNum[0][1] - shelterListNum[j][1])
                if curDist < minDist:
                    j += 1
            for _ in range(len(villageListNum)):
                result.append(0)
            result[villageListNum[0][0] - 1] = shelterListNum[j - 1][0]
            curShelterIndex = j - 1
    else:
        if villageListNum[i][1] <= shelterListNum[0][1]:
            result[villageListNum[i][0] - 1] = \
                shelterListNum[0][0]
        elif villageListNum[i][1] >= shelterListNum[-1][1]:
            result[villageListNum[i][0] - 1] = shelterListNum[-1][0]
        else:
            if abs(villageListNum[i][1] -
                   shelterListNum[curShelterIndex][1]) <=\
                    abs(villageListNum[i][1] -
                        shelterListNum[curShelterIndex + 1][1]):
                result[villageListNum[i][0] - 1] = \
                    result[villageListNum[i - 1][0] - 1]
            else:
                curDist = abs(villageListNum[i][1] -
                              shelterListNum[curShelterIndex + 1][1])
                curShelterIndex += 1
                if len(shelterListNum) > curShelterIndex + 1:
                    nextDist = abs(villageListNum[i][1] -
                                   shelterListNum[curShelterIndex + 1][1])
                    while nextDist < curDist:
                        curDist = nextDist
                        curShelterIndex += 1
                        nextDist = abs(villageListNum[i][1] -
                                       shelterListNum[curShelterIndex + 1][1])
                result[villageListNum[i][0] - 1] = \
                    shelterListNum[curShelterIndex][0]
print(*result)
