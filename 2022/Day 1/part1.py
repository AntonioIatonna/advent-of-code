elfTotals = []
currentTotal = 0

with open('day1Input.txt', 'r') as file:
    
    for line in file:
        if(line.strip()):
            currentTotal = currentTotal + int(line)
        else:
            elfTotals.append(currentTotal)
            currentTotal = 0

    mostCalories = max(elfTotals)    
    print("The top elf has " + str(mostCalories) + " calories.")