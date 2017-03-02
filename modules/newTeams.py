import dataParser, teamPrototypes, teamRanker, statCalculator

teamData = dataParser.initializeTeamData()
statsPrototype = teamPrototypes.stats

def addNewTeam(prototype):
    '''
    list -> list
    PRE: Takes a list of team data
    POST: Adds team and resorts the data.
    '''
    prototype = prototype[:-1]
    print(prototype)
    newTeam = []
    i = 0
    while i < len(statsPrototype):
        #print('i: %d < len(statsPrototype) - 1: %d' % (i, len(prototype) - 1))
        if i == 4:
            appendedElement = str(input('what is the %s?\n>' % prototype[i]))
            newTeam.append(appendedElement)
            break
        appendedElement = float(input('what is the %s?\n>' % prototype[i]))
        newTeam.append(appendedElement)
        i += 1
    return newTeam
