sideA = ""
sideB = ""
totalSum = 0

with open('day3Input.txt', 'r') as file:
    
    for line in file:
        sideA = line[:len(line)//2]
        sideB = line[len(line)//2:]

        for i in range(len(sideA)):
            if sideA[i] in sideB:
                if(ord(sideA[i]) >= 97 and ord(sideA[i]) <= 122):
                    totalSum += (ord(sideA[i]) - 96)
                elif(ord(sideA[i]) >= 41 and ord(sideA[i]) <= 90):
                    totalSum += (ord(sideA[i]) - 38)
                break

    print(totalSum)