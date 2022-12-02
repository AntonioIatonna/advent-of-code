total = 0
winCondition = -1

with open('day2Input.txt', 'r') as file:
    
    for line in file:
        currentRoundScore = 0

        opponent = line[0]
        you = line[2]

        # find win condition
        if(you == 'X'):
            currentRoundScore += 1
        elif(you == 'Y'):
            currentRoundScore += 2
        elif(you == 'Z'):
            currentRoundScore += 3

        # get win condiiton score
        if((opponent == 'A' and you == 'Z') or (opponent == 'B' and you == 'X') or (opponent == 'C' and you == 'Y')):
            pass
        elif((opponent == 'A' and you == 'X') or (opponent == 'B' and you == 'Y') or (opponent == 'C' and you == 'Z')):
            currentRoundScore += 3
        elif((opponent == 'A' and you == 'Y') or (opponent == 'B' and you == 'Z') or (opponent == 'C' and you == 'X')):
            currentRoundScore += 6

        total += currentRoundScore

    print(total)