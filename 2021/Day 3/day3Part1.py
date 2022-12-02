gamma = 0
epsilon = 0
rawData = []

with open('day3Input.txt', 'r') as file:
    
    for line in file:
        rawData.append(line)

size = len(rawData)
unitSize = len(rawData[0]) - 1

for j in range(0, unitSize):
    zeroCounter = 0
    oneCounter = 0
    activeNumber = 0
    for i in range(0, size):
        activeNumber = rawData[i]
        activeNumber = int(activeNumber) // (pow(10,11-j))
        activeNumber = int(activeNumber) % 10
        if(int(activeNumber) == 0):
            zeroCounter += 1
        elif(int(activeNumber) == 1):
            oneCounter += 1

    if(oneCounter > zeroCounter):
        gamma = (gamma * 10) + 1
        epsilon = (epsilon * 10) + 0
    elif(zeroCounter > oneCounter):
        gamma = (gamma * 10) + 0
        epsilon = (epsilon * 10) + 1

gammaDecimal = int(str(gamma),2)
epsilonDecimal = int(str(epsilon),2)

print("Power Consumption: " + str(gammaDecimal * epsilonDecimal))