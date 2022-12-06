file = open('day6Input.txt', 'r')

line = file.readline()

file.close()

for i in range(len(line) - 3):
    if((line[i] != line[i + 1]) and (line[i] != line[i + 2]) and (line[i] != line[i + 3])):
        if((line[i + 1] != line[i + 2]) and (line[i + 1] != line[i + 3])):
            if(line[i + 2] != line[i + 3]):
                break

print(i + 4)