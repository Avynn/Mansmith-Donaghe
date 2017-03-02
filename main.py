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
import newCategory
import newTeams
import teamPrototypes
###/local imports###

###teamData initialization#####
teamData = dataParser.initializeTeamData()
teamDataLength = len(teamData)
statsPrototype = teamPrototypes.stats
###/teamData init######

###teamRanking initialization###


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

#aVar = MetaData.freThrowMadeRankings
#print(aVar)

i = 0
while i < teamDataLength:
    statScore = statCalculator.calculateScores(i, .15, .4, .2, .15, MetaData)
    teamData[i].append(statScore)
    #print(teamData[i][5])
    i += 1
###/teamRanking initialization####


###main loop####
while True:
    userSelection = input('What do you want to do? type help for options.\n>')
    userSelection.lower
    if userSelection == 'category':
        newCategory.addNewCategory(teamData)
    elif userSelection == 'newteam':
        teamData.append(newTeams.addNewTeam(statsPrototype))
        teamDataLength = len(teamData) - 1
        print(teamDataLength + 1)
        statCalculator.calculateScores(43, .15, .4, .2, .15, MetaData)
        teamRanker.sortTeams(teamData)
        print('success!')
        print('\n\n')
    elif userSelection == 'list':
        teamRanker.sortTeams(teamData)
        j = len(teamData) - 1
        while j >= 0:
            print(teamData[j])
            j -= 1
        print('\n\n')
    elif userSelection == 'help':
        print('available commands are:')
        print('category, creates a new category')
        print('newteam, adds a new team')
        print('list, lists current teams in rank order')
        print('quit, quits the app')
        print('\n\n')
    elif userSelection == 'quit':
        break
    else:
        print('need help? type help.')
        print('\n\n')

###/main loop###
