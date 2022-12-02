values = []
counter = 0
sumCounter = 0

with open('day1Input.txt', 'r') as file:
    
    for line in file:
        values.append(int(line))

    size = len(values)
    sums = [0] * (size - 2)

    for i in range(0, size - 1):
        if(values[i] < values[i+1]):
            counter = counter + 1
        else:
            pass
     
    print(counter)

    for j in range(0, size - 2):
        sums[j] = values[j] + values[j+1] + values[j+2]
    
    for k in range(0, len(sums) - 1):
        if(sums[k] < sums[k+1]):
            sumCounter = sumCounter + 1
    
    print(sumCounter)