size = int(input())
sizesList = list(map(int, input().split()))
sizesList.sort()
count = 0
curSize = sizesList[0]
for i in range(0, len(sizesList)):
    if not count and sizesList[i] >= size:
        count += 1
        curSize = sizesList[i]
    if count and sizesList[i] >= curSize + 3:
        count += 1
        curSize = sizesList[i]
print(count)
