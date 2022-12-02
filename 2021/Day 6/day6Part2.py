with open('day6Input.txt', 'r') as file:
    
    fish = file.read().split(",")
    fish = [int(numeric_string) for numeric_string in fish]

    groups = [0] * 9 # create a group for the number of days until birth

    for num in fish: # count number of fish in each group
        groups[num] += 1
    
    for days in range(256):
        activeNumber = groups[0] # set active number to number of fish about to give birth
        for j in range(1, len(groups)):
            groups[j-1] = groups[j] # reduce the number of days for each fish by one
        groups[8] = activeNumber # set group 8 to number of fish who just gave birth, as newborn fish take 8 days rather than 6
        groups[6] += activeNumber # add number of fish who just gave birth to group 6, as the counter begins again
    
    total = 0
    for i in range(0, len(groups)):
        total += groups[i]

    print(total)