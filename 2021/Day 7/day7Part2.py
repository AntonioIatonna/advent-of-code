from statistics import mean

with open('Day 7/day7Input.txt', 'r') as file:
    
    crabs = file.read().split(",")
    crabs = [int(numeric_string) for numeric_string in crabs]

    totalFuel = pow(999,999)

    for i in range(0, max(crabs)):
        fuelUsed = 0
        for j in crabs:
            change = abs(j-i)
            fuelUsed += (change * (change + 1)//2)
        if(fuelUsed < totalFuel):
            totalFuel = fuelUsed

    print(totalFuel)