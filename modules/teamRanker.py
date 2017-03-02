import dataParser, statCalculator, doctest

teamData = dataParser.initializeTeamData()
teamLength = len(teamData) - 1

class MetaData:
    '''
    defines the best and worst stats for each category.
    '''

    freThrowMadeRankings = []
    for i in teamData:
        freThrowMadeRankings.append(i[0])
        freThrowMadeRankings.sort()
    #print(freThrowMadeRankings)

    feilGolPrctRankings = []
    for i in teamData:
        feilGolPrctRankings.append(i[1])
        feilGolPrctRankings.sort()

    rebMarRankings = []
    for i in teamData:
        rebMarRankings.append(i[2])
        rebMarRankings.sort()

    trnOvrMarRankings = []
    for i in teamData:
        trnOvrMarRankings.append(i[3])
        trnOvrMarRankings.sort()

    freThrowMadeRankingsBest = freThrowMadeRankings[len(freThrowMadeRankings) - 1]
    freThrowMadeRankingsWorst = freThrowMadeRankings[0]

    feilGolPrctRankingsBest = feilGolPrctRankings[len(freThrowMadeRankings) - 1]
    feilGolPrctRankingsWorst = feilGolPrctRankings[0]

    rebMarRankingsBest = rebMarRankings[len(freThrowMadeRankings) - 1]
    rebMarRankingsWorst = rebMarRankings[0]

    trnOvrMarRankingsBest = trnOvrMarRankings[len(freThrowMadeRankings) - 1]
    trnOvrMarRankingsWorst = trnOvrMarRankings[0]




i = 0
while i < teamLength:
    statScore = statCalculator.calculateScores(i, .15, .4, .2, 15, MetaData)
    teamData[i].append(statScore)
    i += 1

def findMinimumIndex(aList, pos):
    '''
    list, int -> int
    PRE: takes a list and a position on that list
    POST: returns the position of the lowest value in the fith index of the fith element.
    >>> findMinimumIndex([[0, 0, 0, 0, 0, 3],[0, 0, 0, 0, 0, 5],[0, 0, 0, 0, 0, 2],[0, 0, 0, 0, 0, 8]], 0)
    2
    >>> findMinimumIndex([[0, 0, 0, 0, 0, 12],[0, 0, 0, 0, 0, 78],[0, 0, 0, 0, 0, 45],[0, 0, 0, 0, 0, 20]], 0)
    0
    >>> findMinimumIndex([[0, 0, 0, 0, 0, 0.2],[0, 0, 0, 0, 0, 0.75],[0, 0, 0, 0, 0, 0.89],[0, 0, 0, 0, 0, 0.15]], 0)
    3
    '''
    #print(pos)
    lowest = pos + 1
    while pos < len(aList):
        if pos == len(aList) - 1:
            return lowest
        if aList[pos][-1] <= aList[lowest][-1]:
            #print('PING!')
            lowest = pos
            pos += 1
        else:
            pos += 1
    return lowest

def posSwapper(aList, pos1, pos2):
    '''
    list, int, int -> void
    PRE: takes a list the first position and the position to be swapped
    POST: swaps position 1 with position 2
    >>> posSwapper([12,14], 0, 1)
    [14, 12]
    >>> posSwapper([12,13,14], 0, 2)
    [14, 13, 12]
    >>> posSwapper([11,12,13,14,15], 0, 4)
    [15, 12, 13, 14, 11]
    '''
    toMoveUp = aList[pos1]
    aList[pos1] = aList[pos2]
    aList[pos2] = toMoveUp

    return aList

def sortTeams(aList):
    '''
    list -> void
    PRE: takes a list.
    POST: sorts list by the fith index of all it's indicies.
    '''
    i = 0
    while i < teamLength - 1:
        #print(i)
        posSwapper(aList, i, findMinimumIndex(aList, i))
        i+=1


if __name__ == "__main__":
    doctest.testmod()
