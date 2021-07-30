fin = open('input.txt', 'r', encoding='utf-8')
listPoints = [(0, 0), (0, 0), (0, 0)]
for line in fin.readlines():
    elems = line.split()
    form = 11 - int(elems[2])
    points = int(elems[3])
    listPoints[form] = (listPoints[form][0] + 1, listPoints[form][1] + points)
listPoints = listPoints[::-1]
print(' '.join(map(lambda x: str(x[1] / x[0]) if x[0] else str(0),
                   listPoints)))
