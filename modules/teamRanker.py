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
    #print(pos)
    lowest = 10000
    while True:
        b = pos + 1
        if pos == len(aList) - 2:
            print('position %d, length of list %d' % (pos, len(aList)))
            print('lowest is: %d' % lowest)
            return lowest
        elif aList[pos][5] <= lowest:
            print(str(float(aList[pos][5])) + ' < ' + str(lowest))
            lowest = pos
            print('%d' % aList[lowest][5])
            print('=============')
            pos += 1
#        elif aList[pos][5] <= aList[b][5]:
#            print('%d is less than %d' % (pos, b))
#            print(str(float(aList[pos][5])) + ' < ' + str(float(aList[b][5])))
#            lowest = pos
#            print('%d' % aList[lowest][5])
#            print('===========')
#            pos += 1
        elif aList[pos][5] > lowest:
            print('%d is more than %d' % (pos, b))
            print(str(float(aList[pos][5])) + ' > ' + str(float(aList[b][5])))
            print('%d' % aList[lowest][5])
            print('=========')
            pos += 1
