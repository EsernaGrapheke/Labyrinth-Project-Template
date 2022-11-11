import copy
from time import sleep
import os


def dibujarMatriz(matriz):
    os.system('cls')
    print("Best Solution:")
    for renglon in matriz:
        for columna in renglon:
            print(columna, end='')
        print()
    sleep(0.5)


labyrinth = [['x', 'x', 'x', 'x', 'x', 'x'],
             ['x', ' ', ' ', ' ', 'S', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', 'x', ' ', 'x'],
             ['x', ' ', 'x', ' ', ' ', 'x'],
             ['x', ' ', 'x', ' ', 'x', 'x'],
             ['x', ' ', ' ', 'E', ' ', 'x'],
             ['x', 'x', 'x', 'x', 'x', 'x']]

# labyrinth = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#              ['x', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
#              ['x', ' ', 'x', 'x', ' ', 'x', ' ', 'x'],
#              ['x', ' ', 'x', 'x', ' ', 'x', ' ', 'x'],
#              ['x', ' ', 'x', 'x', ' ', 'x', ' ', 'x'],
#              ['x', 'E', ' ', ' ', ' ', ' ', 'S', 'x'],
#              ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

tempMatrix = copy.deepcopy(labyrinth)

entrance = [0, 0]
salida = [0, 0]
checkpoint = [[]]
saveBoard = []
saveNumberOfSteps = []
numberOfSteps = 0
optimalSteps = 10000
paths = [[]]
numberOfCheckpoints = 10000

row = 0
while row < len(labyrinth):
    column = 0
    while column < len(labyrinth[row]):
        if labyrinth[row][column] == 'E':
            entrance = [row, column]
        elif labyrinth[row][column] == 'S':
            salida = [row, column]
        column += 1
    row += 1

currentLocation = copy.deepcopy(entrance)

pathLeft = True
pathRight = True
pathUp = True
pathDown = True
while numberOfCheckpoints > 0 or pathLeft is True or pathRight is True or pathUp is True or pathDown is True:
    numberOfPaths = 0
    if tempMatrix[currentLocation[0]][currentLocation[1] - 1] == ' ':
        pathLeft = True
        numberOfPaths += 1
    else:
        pathLeft = False
    if tempMatrix[currentLocation[0] - 1][currentLocation[1]] == ' ':
        pathUp = True
        numberOfPaths += 1
    else:
        pathUp = False
    if tempMatrix[currentLocation[0]][currentLocation[1] + 1] == ' ':
        pathRight = True
        numberOfPaths += 1
    else:
        pathRight = False
    if tempMatrix[currentLocation[0] + 1][currentLocation[1]] == ' ':
        pathDown = True
        numberOfPaths += 1
    else:
        pathDown = False

    if numberOfPaths > 1 and currentLocation != checkpoint[-1]:
        tempList = copy.deepcopy(currentLocation)
        checkpoint.append(tempList)
        paths.append([pathLeft, pathUp, pathRight, pathDown])
        numberOfCheckpoints = len(checkpoint)
        tempList = copy.deepcopy(tempMatrix)
        saveBoard.append(tempList)
        saveNumberOfSteps.append(numberOfSteps)

    if not checkpoint[0]:
        checkpoint.pop(0)
        paths.pop(0)
        numberOfCheckpoints = len(checkpoint)

    if currentLocation == checkpoint[-1]:
        pathLeft = paths[-1][0]
        pathUp = paths[-1][1]
        pathRight = paths[-1][2]
        pathDown = paths[-1][3]

    if pathLeft is True:
        if currentLocation == checkpoint[-1]:
            paths[-1][0] = False
        currentLocation[1] -= 1
        numberOfSteps += 1
        tempMatrix[currentLocation[0]][currentLocation[1]] = '.'
        dibujarMatriz(tempMatrix)
    elif pathUp is True:
        if currentLocation == checkpoint[-1]:
            paths[-1][1] = False
        currentLocation[0] -= 1
        numberOfSteps += 1
        tempMatrix[currentLocation[0]][currentLocation[1]] = '.'
        dibujarMatriz(tempMatrix)
    elif pathRight is True:
        if currentLocation == checkpoint[-1]:
            paths[-1][2] = False
        currentLocation[1] += 1
        numberOfSteps += 1
        tempMatrix[currentLocation[0]][currentLocation[1]] = '.'
        dibujarMatriz(tempMatrix)
    elif pathDown is True:
        if currentLocation == checkpoint[-1]:
            paths[-1][3] = False
        currentLocation[0] += 1
        numberOfSteps += 1
        tempMatrix[currentLocation[0]][currentLocation[1]] = '.'
        dibujarMatriz(tempMatrix)
    elif tempMatrix[currentLocation[0]][currentLocation[1] - 1] == 'S' or tempMatrix[currentLocation[0] - 1][currentLocation[1]] == 'S' or tempMatrix[currentLocation[0]][currentLocation[1] + 1] == 'S' or tempMatrix[currentLocation[0] + 1][currentLocation[1]] == 'S':
        if numberOfSteps < optimalSteps:
            optimalSteps = numberOfSteps
            solution = copy.deepcopy(tempMatrix)
        if len(checkpoint) > 0:
            currentLocation = copy.deepcopy(checkpoint[-1])
            tempMatrix = copy.deepcopy(saveBoard[-1])
            numberOfCheckpoints = len(checkpoint)
            numberOfSteps = saveNumberOfSteps[-1]
        else:
            numberOfCheckpoints = 0
    else:
        if len(checkpoint) > 0:
            currentLocation = copy.deepcopy(checkpoint[-1])
            tempMatrix = copy.deepcopy(saveBoard[-1])
            numberOfCheckpoints = len(checkpoint)
            numberOfSteps = saveNumberOfSteps[-1]
        else:
            numberOfCheckpoints = 0

    if currentLocation == checkpoint[-1]:
        if paths[-1] == [False, False, False, False]:
            checkpoint = copy.deepcopy(checkpoint[:-1])
            paths = copy.deepcopy(paths[:-1])
            saveBoard = copy.deepcopy(saveBoard[:-1])
            saveNumberOfSteps = copy.deepcopy(saveNumberOfSteps[:-1])
            numberOfCheckpoints = len(checkpoint)
            if numberOfCheckpoints > 0:
                currentLocation = copy.deepcopy(checkpoint[-1])
                tempMatrix = copy.deepcopy(saveBoard[-1])
                numberOfSteps = saveNumberOfSteps[-1]


dibujarMatriz(solution)
print("Optimum number of steps:", optimalSteps)
