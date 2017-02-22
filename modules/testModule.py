aList = []

def appendList(i, aList):
    returnedList = []
    if i <= 10:
        returnedList.append('hello')
        return appendList(i + 1, aList + returnedList)
    else:
        return aList + returnedList

print(appendList(0, aList))
