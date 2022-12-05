count = 0
stacks = dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(1,10):
    stacks[i] = []

with open('day5Input.txt', 'r') as file:

    lineslist = file.readlines()
    for i in range(1, 35, 4):
        count +=1
        for line in reversed(lineslist[:8]):
            if(line[i] != " "):
                stacks[count].append(line[i])
file.close()

with open('day5Input.txt', 'r') as file:
    lineslist = file.readlines()
    for line in (lineslist[10:]):
        if(len(line) == 19):      
            moveNum = line[5]
            moveFrom = line[12]
            moveTo = line[17]
        elif(len(line) == 20):
            moveNum = line[5:7]
            moveFrom = line[13]
            moveTo = line[18]
    
        for i in range(1, int(moveNum) + 1):
            stacks[int(moveTo)].append(stacks[int(moveFrom)].pop())

file.close()

for i in range(1,10):
    print(stacks[i].pop(), end = "")