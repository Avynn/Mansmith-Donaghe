import os.path

path = 'store/'
if __name__ == "__main__":
    path = '../store/'

path2 = 'savedData/'
if __name__ == "__main__":
   path2 = '../savedData/'

###########note#############
'''
do not use these JSON functions for normal api usage
they are just for converting the sports stats
'''

def stringSlicer(string, pos, enditerand):
    """
    string, int, int -> string
    PRE: This function takes in a string and a position within it.
    POST: This function returns a slice of the string between a colon and a
    comma.
    """
    pos += 2
    stringOut = ""
    while True:
        if enditerand == 5 and string[pos] == '}':
            stringOut = stringOut[:len(stringOut) - 2]
            return stringOut, pos
        elif string[pos] == ',':
            return stringOut, pos
        else:
            stringOut += string[pos]
            pos += 1



def renderJSONElement(i):
    '''
    int -> str
    This function is used in order to actually generate  a string for multiple
    teams when looping through the documents.
    PRE: JSON data is fed into this function.
    POST: one string with the contents of a JSON file is produced
    '''
    #opens file
    openedDataBuffer = open(path + str(i) + '.json', 'r')
    #reads file
    openedData = openedDataBuffer.read()
    j = 0
    string = ''
    while j < len(openedData):
        string = string + openedData[j]
        j = j + 1
    openedDataBuffer.close()
    return string

def parseJSONStoreData(i):
    '''
    int, list -> list
    since this function is only for the data in store, first argument should always be 2.
    PRE: takes the value of the first document name in store as well as an empty list
    POST: One list containing strings where every element is JSON represented as a string.
    '''
    #function calls self with modified iterand and updated list
    inList = []
    if os.path.exists(path + str(i) + '.json'):
        JSONElement = renderJSONElement(i)
        j = 0
        k = 0
        returnValues = []
        while j < len(JSONElement):
            if JSONElement[j] == ':':
                returnValuestoAppend, j = stringSlicer(JSONElement, j, k)
                returnValues.append(returnValuestoAppend)
                k += 1
            else:
                j +=1
        return returnValues
    else:
        return "NULL"

def dataCleaner(i):
    '''
    int -> list
    PRE: takes list.
    POST: removes extraneous quotations around data.
    '''
    cleanArray = []
    element = parseJSONStoreData(i)
    for j in range(0,4):
        cleanArray.append(float(element[j][1:len(element[j]) - 1]))
    cleanArray.append(element[5][1:])
    return cleanArray


def initializeJSONTeamData():
    '''
    void -> list
    PRE: utilizes previously written functions.
    POST: populates an array with team data from store.
    '''
    teamData = []
    i = 2
    while True:
        if os.path.exists(path + str(i) + '.json'):
            teamData.append(dataCleaner(i))
            i += 1
        else:
            return teamData

#############/note#############

def initializeTeamData():
    '''
    void -> list
    POST: returns a list with team data from new saved data folder.
    '''
    returnedData = []
    savedDataList = [name for name in os.listdir(path2) if os.path.isfile(os.path.join(path2, name))]
    savedDataList.sort()
    filePath = path2 + savedDataList[-1]
    openedData = open(filePath, 'r')
    for line in openedData:
        line = line.strip('[')
        line = line.strip('\n')
        line = line.strip(']')
        line = line.split(',')
        line[1] = line[1].strip(' ')
        line[2] = line[2].strip(' ')
        line[3] = line[3].strip(' ')
        line[4] = line[4].strip(' ')
        line[4] = line[4].strip("'")
        line[0] = float(line[0])
        line[1] = float(line[1])
        line[2] = float(line[2])
        line[3] = float(line[3])
        returnedData.append(line)
    openedData.close()
    return returnedData

def initializeTeamNameList():
    '''
    '''
    returnedData = []
    openedData = open('modules/teamNames.csv', 'r')
    for line in openedData:
        line = line.strip('\n')
        returnedData.append(line)
    openedData.close()
    return returnedData
