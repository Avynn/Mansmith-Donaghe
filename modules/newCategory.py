import dataParser, teamPrototypes

teamData = dataParser.initializeTeamData()

prototype = teamPrototypes.stats

def addNewCategory(dataList):
    '''
    list -> void
    PRE: takes a list with team data.
    POST: append new category to teamData.
    '''
    #initialization phase
    print('WARNING: this function will not automatically factor in new stat categories.')
    print('the stat calculator must be modified before new stat categories are factored.\n\n')
    categoryName = input('What is the name of your category? \n>')
    secondToLastPrototypeIndexValue = prototype[-2]
    prototype[-2] = categoryName
    lastPrototypeIndexValue = prototype[-1]
    prototype[-1] = secondToLastPrototypeIndexValue
    prototype.append(lastPrototypeIndexValue)
    #datatype input phase
    categoryType = 'NULL'
    while True:
        categoryType = input('What is the type of the data? \n>')
        if categoryType == 'int' or categoryType == 'float' or categoryType == 'str':
            break
        else:
            print('please enter a proper datatype:\nint, float or str\n')

    print(prototype)
    #data entry phase
    i = 0
    while i < len(dataList):
        print('============')
        print(dataList[i])
        if categoryType == 'int':
            print('WARNING: change new teams module before adding a new team.')
            appendedEntry = (int(input('enter value for %s: ' % dataList[i][4])))
        elif categoryType == 'float':
            appendedEntry = (float(input('enter value for %s: ' % dataList[i][4])))
        elif categoryType == 'str':
            print('WARNING: change new teams module before adding a new team.')
            appendedEntry = (float(input('enter value for %s: ' % dataList[i][4])))

        lastIndexValue = dataList[i][-1]
        dataList[i][-1] = appendedEntry
        dataList[i].append(lastIndexValue)
        print(dataList[i])
        i += 1
