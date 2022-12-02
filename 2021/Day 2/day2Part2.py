hPos = 0
vPos = 0
directions = []
aim = 0

with open('day2Input.txt', 'r') as file:
    
    for line in file:
        directions.append(line)

    size = len(directions)
    compassDirections = [0] * size
    numberDirections = [0] * size

    for i in range(0, size):
        compassDirections[i] = directions[i].split(" ", 1)[0]
        numberDirections[i] = directions[i].split(" ", 1)[1]

    for j in range(0, size):
        numberDirections[j] = int(numberDirections[j])
    
    for k in range(0, size):
        if(compassDirections[k] == 'forward'):
            hPos = hPos + numberDirections[k]
            vPos = vPos + (numberDirections[k] * aim)
        elif(compassDirections[k] == 'up'):
            aim = aim - numberDirections[k]
        elif(compassDirections[k] == 'down'):
            aim = aim + numberDirections[k]
        else:
            pass
    
    print(vPos * hPos)
    