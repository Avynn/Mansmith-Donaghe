import dataParser

class MetaData:
    '''
    defines the best and worst stats for each category.
    '''
    teamData = dataParser.initializeTeamData()
    #print(teamData)

    freThrowMadeRankings = []
    for i in teamData:
        freThrowMadeRankings.append(i[0])
        freThrowMadeRankings.sort()
    print(freThrowMadeRankings)

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

def calculateScores(iteration, freThrowMadeWeight, feilGolPrctWeight, rebMarWeight, trnOvrMarWeight):
    '''
    int, float, float, float, float -> float
    PRE: Takes the iteration and the weights of the stats.
    POST: using the iteration the function calculates the coresponding team's "score".
    '''
    meta = MetaData()

    FreThrowMadeOutputRaw = (meta.teamData[iteration][0] - meta.freThrowMadeRankingsWorst)/(meta.freThrowMadeRankingsBest - meta.freThrowMadeRankingsWorst)
    FreThrowMadeOutput = FreThrowMadeOutputRaw * freThrowMadeWeight

    feilGolPrctOutputRaw = (meta.teamData[iteration][1] - meta.feilGolPrctRankingsWorst)/(meta.feilGolPrctRankingsBest - meta.feilGolPrctRankingsWorst)
    feilGolPrctOutput = feilGolPrctOutputRaw * feilGolPrctWeight

    rebMarOutputRaw = (meta.teamData[iteration][2] - meta.rebMarRankingsWorst)/(meta.rebMarRankingsBest - meta.rebMarRankingsWorst)
    rebMarOutput = rebMarOutputRaw * rebMarWeight

    trnOvrMarOutputRaw = (meta.teamData[iteration][3] - meta.trnOvrMarRankingsWorst)/(meta.trnOvrMarRankingsBest - meta.trnOvrMarRankingsWorst)
    trnOvrMarOutput = trnOvrMarOutputRaw * trnOvrMarWeight

    return FreThrowMadeOutput + feilGolPrctOutput + rebMarOutput + trnOvrMarOutput
