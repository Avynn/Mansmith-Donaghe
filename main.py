###global imports###
import os.path
import sys
###/global imports###

###local imports###
path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

import statCalculator
import dataParser
import teamRanker
###/local imports###


teamData = dataParser.initializeTeamData()

i = 0
while i < 43:
    statScore = statCalculator.calculateScores(i, .15, .4, .2, 15)
    teamData[i].append(statScore)
    i += 1

#print(teamData)

print(teamRanker.findMinimumIndex(teamData, 0))
