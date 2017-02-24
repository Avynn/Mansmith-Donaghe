import dataParser, statCalculator, doctest

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
    >>> findMinimumIndex([[0, 0 ,0, 0, 0, 3],[0, 0, 0, 0, 0, 5],[0, 0, 0, 0, 0, 2],[0, 0, 0, 0, 0, 8]], 0)
    2
    >>> findMinimumIndex([[0, 0 ,0, 0, 0, 12],[0, 0, 0, 0, 0, 78],[0, 0, 0, 0, 0, 45],[0, 0, 0, 0, 0, 20]], 0)
    0
    >>> findMinimumIndex([[0, 0 ,0, 0, 0, 0.2],[0, 0, 0, 0, 0, 0.75],[0, 0, 0, 0, 0, 0.89],[0, 0, 0, 0, 0, 0.15]], 0)
    3
    '''
    #print(pos)
    lowest = pos + 1
    while pos < len(aList):
        b = pos + 1
        if aList[pos][5] <= aList[lowest][5]:
            lowest = pos
            pos += 1
        else:
            pos += 1
    return lowest

if __name__ == "__main__":
    doctest.testmod()
