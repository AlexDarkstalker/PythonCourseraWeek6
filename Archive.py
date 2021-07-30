string = input()
S = int(string.split()[0])
numUsers = int(string.split()[1])
listUser = []
count = 0
for i in range(0, numUsers):
    curUser = int(input())
    listUser.append(curUser)
listUser.sort()
for i in listUser:
    if S - i >= 0:
        count += 1
        S = S - i
print(count)
