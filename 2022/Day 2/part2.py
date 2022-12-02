total = 0
winCondition = -1

with open('day2Input.txt', 'r') as file:
    
    for line in file:
        currentRoundScore = 0

        opponent = line[0]
        you = line[2]
        
        # set choice to win condition
        if(you == 'X'):
            if(opponent == 'A'):
                you = 'Z'
            elif(opponent == 'B'):
                you = 'X'
            elif(opponent == 'C'):
                you = 'Y'
        elif(you == 'Y'):
            if(opponent == 'A'):
                you = 'X'
            elif(opponent == 'B'):
                you = 'Y'
            elif(opponent == 'C'):
                you = 'Z'
        elif(you == 'Z'):
            if(opponent == 'A'):
                you = 'Y'
            elif(opponent == 'B'):
                you = 'Z'
            elif(opponent == 'C'):
                you = 'X'

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