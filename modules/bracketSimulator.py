def runGame(team1, team2):
    team1score = team1[5]
    team2score = team2[5]
    if team1score > team2score:
        return team1
    else:
        return team2

def runDivision(divisionBracketToReduce):
    '''
    list -> list
    PRE: takes division bracket.
    POST: returns the winner of the division.
    '''
    round1 = divisionBracketToReduce
    round2 = []
    round3 = []
    i = 0
    j = len(round1) - 1
    print('division: ', i + 1)
    for teams in divisionBracketToReduce:
        print(teams)
    #round1
    print('round 1')
    while i < j:
        print(round1[i])
        print(round1[j])
        print('=========')
        round2.append(runGame(round1[i], round1[j]))
        i += 1
        j -= 1
    #round2
    print('round 2')
    k = 0
    while k < len(round2) - 1:
        n = k + 1
        print(round2[k])
        print(round2[n])
        print('=========')
        round3.append(runGame(round2[k], round2[n]))
        k += 2
    #round3
    print('round 3')
    print(round3[0])
    print(round3[1])
    print('=========')
    print(runGame(round3[0], round3[1]))
    return runGame(round3[0], round3[1])


def simulateBrackets(teams):
    '''
    List -> list
    PRE: takes a list of teams.
    POST: returns a winner and overal bracket based upon the output values of the teams.
    '''
    print('welcome to the bracket simulator let\'s begin seeding')
    tmpTeams = teams
    finalFour = []
    for i in range(0,4):
        print('Seeding for division: ', i + 1)
        divisionBracket = []
        for i in range(1,17):
            print('here is the roster of teams:')
            j = 0
            for team in tmpTeams:
                j += 1
                print(str(j) + '. ' + team[4])
            try:
                divisionappend = int(input('now choose a team by it\'s number value:\n>'))
            except:
                print('please enter an int.')
            divisionappend -= 1
            divisionBracket.append(tmpTeams[divisionappend])
            del tmpTeams[divisionappend]
        finalFour.append(runDivision(divisionBracket))
        print(finalFour)
        break
