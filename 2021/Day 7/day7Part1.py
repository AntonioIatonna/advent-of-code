with open('Day 7/day7Input.txt', 'r') as file:
    
    crabs = file.read().split(",")
    crabs = [int(numeric_string) for numeric_string in crabs]

    for i in range(len(crabs) - 1):
        for j in range(0, len(crabs) - i - 1):
            if(crabs[j] > crabs[j + 1]):
                crabs[j], crabs[j + 1] = crabs[j + 1], crabs[j]
    
    middleIndex = (len(crabs) - 1)/2
    wantedNumber = crabs[int(middleIndex)]
    fuelUsed = 0

    for i in range(0, len(crabs)):
        while(crabs[i] > wantedNumber):
            crabs[i] -= 1
            fuelUsed += 1
        while(crabs[i] < wantedNumber):
            crabs[i] += 1
            fuelUsed += 1

    print(fuelUsed)