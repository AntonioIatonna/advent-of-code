with open('Day 9/sample.txt', 'r') as file:

    coordinates =[[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]]

    for i in range(0,5):
        line = file.readline()
        for j in range(0,len(line)):
            line = str(line).split()
            coordinates[i][j] = line[j]
    
    print(coordinates)