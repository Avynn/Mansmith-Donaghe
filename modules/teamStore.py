import dataParser, datetime, os

teamData = dataParser.initializeTeamData()
path = '../savedData/'
#if __name__ == '__main__':
#    path = '../savedData/'

def cleanTeamData(teams):
    '''
    list -> void
    PRE: takes a list.
    POST: chops the last index off.
    '''
    returnValues = []
    for team in teams:
        team = team[:5]
        returnValues.append(team)
    return returnValues

def saveData(teams):
    '''
    list -> void
    PRE: takes list
    POST: saves list to a .txt document.
    '''
    dateAndTimeString = str(datetime.datetime.now())
    fileNameSplit = dateAndTimeString.split(' ')
    fileName = fileNameSplit[0] + fileNameSplit[1]
    try:
        filePath = os.path.join(path, fileName)
    except:
        os.mkdirs(path)
    print('saving at path: ', filePath)
    outData = open(filePath, 'w+')
    print(path + fileName + '.txt')
    #print(teamData)
    for team in teams:
        print(team, file = outData)
    outData.close()

def saveTeamNames(teams):
    '''
    list -> void
    PRE: takes list
    POST: saves list to a .csv document.
    '''
    print('updating team names...')
    outData = open('modules/teamNames.csv', 'w')
    for team in teams:
        print(team[4], file = outData)

    outData.close()
saveTeamNames(teamData)
