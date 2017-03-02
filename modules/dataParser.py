import os.path

path = 'store/'
if __name__ == "__main__":
    path = '../store/'

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


def initializeTeamData():
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
