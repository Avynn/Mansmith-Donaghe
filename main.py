###global imports###
import os.path
import sys
###/global imports###

###local imports###
path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'modules'))
if not path in sys.path:
    sys.path.insert(1, path)
del path
###/local imports###

import dataParser

teamData = dataParser.initializeTeamData()

i = 0
while i < len(teamData):
    print(teamData[i])
    i += 1
