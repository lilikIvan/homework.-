myList = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(myList):
    if myList[index] > 0:
        print(myList[index])
        index += 1
        continue

    if myList[index] == 0:
        index += 1
        continue

    if myList[index] < 0:
        break