with open('day4Input.txt', 'r') as file:
    
    line = file.readline()
    calledNumbers = line.split(",")

    bigMin = []
    id = 0

    while(True):
        card = []
        line = file.readline()
        if(line == "stop"):
            break
        for i in range(0,5):
            row = []
            line = file.readline()
            row = line.split(" ")
            for j in range(0,5):
                if(row[j] == ""):
                    row.pop(j)
            row[4] = row[4].replace("\n", "")
            card.append(row)

        if(id == 45):
            print(card)

        rowCounter = [0] * 5

        for k in range(0,5):
            for j in range(0,5):
                for i in range(0,len(calledNumbers)):
                    if(card[k][j] == calledNumbers[i]):
                        if(rowCounter[k] < i):
                            rowCounter[k] = i

        columnCounter = [0] * 5

        for k in range(0,5):
            for j in range(0,5):
                for i in range(0,len(calledNumbers)):
                    if(card[j][k] == calledNumbers[i]):
                        if(columnCounter[k] < i):
                            columnCounter[k] = i

        combinedArray = rowCounter + columnCounter

        min = 100
        for i in range(0,10):
            if(min > combinedArray[i]):
                min = combinedArray[i]
        
        bigMin.append(min)

        id += 1

minOfBigMin = 100
for i in range(0,len(bigMin)):
    if(minOfBigMin > bigMin[i]):
        minOfBigMin = bigMin[i]
        print("Board number " + str(i))

print(minOfBigMin)