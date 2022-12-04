elves = []
bagOne = ""
bagTwo = ""
bagThree = ""
totalSum = 0

with open('day3Input.txt', 'r') as file:
    
    for line in file:
        elves.append(line)

    file.close()

    for i in range(0, len(elves), 3):
        bagOne = elves[i]
        bagTwo = elves[i + 1]
        bagThree = elves[i + 2]

        for i in range(len(bagOne)):
            if((bagOne[i] in bagTwo) and (bagOne[i] in bagThree)):
                if(ord(bagOne[i]) >= 97 and ord(bagOne[i]) <= 122):
                    totalSum += (ord(bagOne[i]) - 96)
                elif(ord(bagOne[i]) >= 41 and ord(bagOne[i]) <= 90):
                    totalSum += (ord(bagOne[i]) - 38)
                break

    print(totalSum)