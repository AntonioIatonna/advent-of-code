with open('day4Input.txt', 'r') as file:

    winningBoard = [[81, 23, 6, 14, 26], [86, 42, 82, 95, 85], [77, 52, 38, 2, 33], [69, 98, 54, 37, 4], [78, 39, 3, 75, 80]]
    
    line = file.readline()
    calledNumbers = line.split(",")
    winNum = 0

    for i in range(0,5):
        for j in range(0,5):
            for k in range(0, 26):
                if(winningBoard[i][j] == int(calledNumbers[k])):
                    print(winningBoard)
                    if(k == 25):
                        winNum = int(calledNumbers[k])
                    print(k)
                    winningBoard[i][j] = 0
    
    print(winningBoard)
    sum = 0

    for i in range(0,5):
        for j in range(0,5):
            sum = sum + winningBoard[i][j]

    print(winNum)
    print(sum)
    print(int(sum*winNum))