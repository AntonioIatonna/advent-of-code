elfTotals = []
currentTotal = 0

with open('day1Input.txt', 'r') as file:
    
    for line in file:
        if(line.strip()):
            currentTotal = currentTotal + int(line)
        else:
            elfTotals.append(currentTotal)
            currentTotal = 0

    grandTotal = 0
    for i in range(3):
        mostCalories = max(elfTotals)
        grandTotal = grandTotal + mostCalories
        elfTotals.remove(mostCalories)
    
    print("The total among the top 3 is " + str(grandTotal))