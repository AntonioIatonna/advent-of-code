with open('day4Input.txt', 'r') as file:

    winningBoard = [[87, 90, 16, 56, 67], [41, 75, 89, 1, 80], [22, 62, 5, 45, 69], [28, 36, 19, 96, 71], [26, 63, 88, 76, 31]]
    
    line = file.readline()
    calledNumbers = line.split(",")
    winNum = 0

    for i in range(0,5):
        for j in range(0,5):
            for k in range(0, 86):
                if(winningBoard[i][j] == int(calledNumbers[k])):
                    print(winningBoard)
                    if(k == 85):
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