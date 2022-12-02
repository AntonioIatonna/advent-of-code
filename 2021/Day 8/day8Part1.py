with open('Day 8/day8Input.txt', 'r') as file:
    
    # 1 = cf len(2)
    # 4 = bcdf len(4)
    # 7 = acf len(3)
    # 8 = abcdefg len(7) 
    counter = 0

    for j in range(0, 200):
        line = file.readline()
        result = line.split(' | ')[1:3]
        result = result[0].split(" ")

        for i in range(len(result) - 1): # check for first three numbers in output
            if(len(result[i]) == 2 or len(result[i]) == 4 or len(result[i]) == 3 or len(result[i]) == 7):
                counter +=1
            else:
                pass
        if(len(result[3]) == 3 or len(result[3]) == 5 or len(result[3]) == 4 or len(result[3]) == 8): # check for final character in output (includes newline so length must be one higher)  
            counter += 1      
    
    print(counter)