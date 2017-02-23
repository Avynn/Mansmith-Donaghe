import dataParser, statCalculator

teamData = dataParser.initializeTeamData()

i = 0
while i < 43:
    statScore = statCalculator.calculateScores(i, .15, .4, .2, 15)
    teamData[i].append(statScore)
    i += 1

def findMinimumIndex(aList, pos):
    '''
    PRE: takes a list and a position on that list
    POST: returns the position of the lowest value
    '''
    lowest = 0
    while True:
        b = pos + 1
        if pos == len(aList) - 2:
            print('ping!')
            return lowest
        elif aList[pos][5] <= aList[b][5]:
            lowest = pos
            pos += 1
        else:
            lowest = b
            pos += 1

findMinimumIndex(teamData, 0)
