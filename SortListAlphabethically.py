fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
listPuples = []
for line in fin.readlines():
    elems = list(map(str, line.split()))
    listPuples.append((elems[0], elems[1], elems[3]))
listPuples.sort(key=lambda x: x[0])
for puple in listPuples:
    print(puple[0], puple[1], puple[2], file=fout)
fin.close()
fout.close()
