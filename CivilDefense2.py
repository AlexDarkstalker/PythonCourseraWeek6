numVillage = int(input())
villageList = map(int, input().split())
numShelters = int(input())
listShelters = list(map(int, input().split()))

for i in range(len(listShelters)):
    listShelters[i] = [i + 1, listShelters[i]]

listShelters.sort(key=lambda x: x[1])


def find_value(x):
    if (x < listShelters[0][1]):
        return listShelters[0][0]
    if (x > listShelters[-1][1]):
        return listShelters[-1][0]
    l = 0
    r = len(listShelters) - 1
    # listShelters[l][1] < x
    while (r - l > 1):
        numShelters = (r + l) >> 1
        if (listShelters[numShelters][1] < x):
            l = numShelters
        else:
            r = numShelters
    if (x - listShelters[l][1] < listShelters[r][1] - x):
        return listShelters[l][0]
    else:
        return listShelters[r][0]


print(*[find_value(v) for v in villageList])
