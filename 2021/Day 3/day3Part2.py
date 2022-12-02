rawDataA = []
rawDataB = []

with open('day3Input.txt', 'r') as file:
    
    for line in file:
        rawDataA.append(line)
        rawDataB.append(line)

size = len(rawDataA)
unitSize = len(rawDataA[0])

for j in range(0, unitSize):
    zeroCounter = 0
    oneCounter = 0
    activeNumber = 0
    popIfOne = []
    popIfZero = []
    for i in range(0, size):
        activeNumber = rawDataA[i]
        activeNumber = int(activeNumber) // (pow(10,11-j))
        activeNumber = int(activeNumber) % 10
        if(int(activeNumber) == 0):
            zeroCounter += 1
            popIfOne.append(i)
        elif(int(activeNumber) == 1):
            oneCounter += 1
            popIfZero.append(i)

    if(oneCounter > zeroCounter):
        for k in range(0, len(popIfOne)):
            rawDataA[popIfOne[k]] = 0
        rawDataA = list(filter(lambda num: num != 0, rawDataA))
        print("Removed zeros in position " + str(j))
    elif(zeroCounter > oneCounter):
        for k in range(0, len(popIfZero)):
            rawDataA[popIfZero[k]] = 0
        rawDataA = list(filter(lambda num: num != 0, rawDataA))
        print("Removed ones in position " + str(j))
    elif(zeroCounter == oneCounter):
        for k in range(0, len(popIfOne)):
            rawDataA[popIfOne[k]] = 0
        rawDataA = list(filter(lambda num: num != 0, rawDataA))
        print("Removed zeros in position " + str(j))
    
    size = len(rawDataA)

    if(size == 1):
        break

oxygenGeneratorRating = rawDataA[0]

size = len(rawDataB)
unitSize = len(rawDataB[0])

for j in range(0, unitSize):
    zeroCounter = 0
    oneCounter = 0
    activeNumber = 0
    popIfOne = []
    popIfZero = []
    for i in range(0, size):
        activeNumber = rawDataB[i]
        activeNumber = int(activeNumber) // (pow(10,11-j))
        activeNumber = int(activeNumber) % 10
        if(int(activeNumber) == 0):
            zeroCounter += 1
            popIfOne.append(i)
        elif(int(activeNumber) == 1):
            oneCounter += 1
            popIfZero.append(i)
    
    if(oneCounter < zeroCounter):
        for k in range(0, len(popIfOne)):
            rawDataB[popIfOne[k]] = 0
        rawDataB = list(filter(lambda num: num != 0, rawDataB))
        print("Removed zeros in position " + str(j))
    elif(zeroCounter < oneCounter):
        for k in range(0, len(popIfZero)):
            rawDataB[popIfZero[k]] = 0
        rawDataB = list(filter(lambda num: num != 0, rawDataB))
        print("Removed ones in position " + str(j))
    elif(zeroCounter == oneCounter):
        for k in range(0, len(popIfZero)):
            rawDataB[popIfZero[k]] = 0
        rawDataB = list(filter(lambda num: num != 0, rawDataB))
        print("Removed ones in position " + str(j))
    
    size = len(rawDataB)

    if(size == 1):
        break

carbonScrubberRating = rawDataB[0]

oxygenGeneratorRating = int(str(oxygenGeneratorRating),2)
carbonScrubberRating = int(str(carbonScrubberRating),2)

print("Life support rating: " + str(oxygenGeneratorRating * carbonScrubberRating))