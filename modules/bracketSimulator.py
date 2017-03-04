def runDivision(divisionBracket):
    round1 = divisionBracket
    round2 = []
    round3 = []
    i = 0
    j = 16
    

def simulateBrackets(teams):
    print('welcome to the bracket simulator let\'s begin seeding')
    tmpTeams = teams
    finalFour = []
    for i in range(0,4):
        print('Seeding for division: ', i + 1)
        divisionBracket = []
        for i in range(1,16):
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
        break
