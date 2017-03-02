import dataParser

def calculateScores(iteration, freThrowMadeWeight, feilGolPrctWeight, rebMarWeight, trnOvrMarWeight, meta):
    '''
    int, float, float, float, float -> float
    PRE: Takes the iteration and the weights of the stats.
    POST: using the iteration the function calculates the coresponding team's "score".
    '''

    FreThrowMadeOutputRaw = (meta.teamData[iteration][0] - meta.freThrowMadeRankingsWorst)/(meta.freThrowMadeRankingsBest - meta.freThrowMadeRankingsWorst)
    FreThrowMadeOutput = FreThrowMadeOutputRaw * freThrowMadeWeight

    feilGolPrctOutputRaw = (meta.teamData[iteration][1] - meta.feilGolPrctRankingsWorst)/(meta.feilGolPrctRankingsBest - meta.feilGolPrctRankingsWorst)
    feilGolPrctOutput = feilGolPrctOutputRaw * feilGolPrctWeight

    rebMarOutputRaw = (meta.teamData[iteration][2] - meta.rebMarRankingsWorst)/(meta.rebMarRankingsBest - meta.rebMarRankingsWorst)
    rebMarOutput = rebMarOutputRaw * rebMarWeight

    trnOvrMarOutputRaw = (meta.teamData[iteration][3] - meta.trnOvrMarRankingsWorst)/(meta.trnOvrMarRankingsBest - meta.trnOvrMarRankingsWorst)
    trnOvrMarOutput = trnOvrMarOutputRaw * trnOvrMarWeight
