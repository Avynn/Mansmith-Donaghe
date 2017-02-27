import dataParser

teamData = dataParser.initializeTeamData()

prototype = ['Free Throws Made', 'field Goal Percent', 'Rebound Margin', 'Turnover Margin', 'name', 'score']

def addNewCategory(dataList):
    '''
    list -> list
    PRE: takes a list with team data.
    POST: append new category to teamData.
    '''
    categoryName = input('What is the name of your category? \n>')
    prototype.append(categoryName)
    #datatype input phase
    categoryType = 'NULL'
    while True:
        categoryType = input('What is the type of the data? \n>')
        if categoryType == 'int' or categoryType == 'float' or categoryType == 'str':
            break
        else:
            print('please enter a proper datatype \nint, float or str\n')

    print(prototype)
    i = 0
    while i < len(dataList):
        if categoryType == 'int':
            appendedEntry = (int(input('enter value for %s: ' % dataList[i][4])))
        elif categoryType == 'float':
            appendedEntry = (float(input('enter value for %s: ' % dataList[i][4])))
        elif categoryType == 'str':
            appendedEntry = (float(input('enter value for %s: ' % dataList[i][4])))

        dataList[i].append(appendedEntry)
        print(dataList[i])
        i += 1

addNewCategory(teamData)
