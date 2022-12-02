with open('Day 8/day8Input.txt', 'r') as file:
    
    # 1 = cf len(2)
    # 4 = bcdf len(4)
    # 7 = acf len(3)
    # 8 = abcdefg len(7) 

    totalValue = 0

    for j in range(0, 200):
        zero, one, two, three, four, five, six, seven, eight, nine = "null", "null", "null", "null", "null", "null", "null", "null", "null", "null"

        line = file.readline()
        result = line.split(" ")
        result.remove("|")

        for i in range(0, 10): # get known values first
            if(len(result[i]) == 2): # find known pattern of one
                one = list(result[i])
            elif(len(result[i]) == 4): # find known pattern of four
                four = list(result[i])
            elif(len(result[i]) == 3): # find known pattern of seven
                seven = list(result[i])
            elif(len(result[i]) == 7): # find known pattern of eight
                eight = list(result[i])
            else:
                pass

        for i in range(0,10): # check unknowns against known values
            if((len(result[i]) == 2) or (len(result[i]) == 4) or (len(result[i]) == 3) or (len(result[i]) == 7)):
                pass
            if(len(result[i]) == 6): # differentiate between length of 6 for zero, six, and nine
                if ((one[0] in result[i]) and (one[1] in result[i])):
                    if((four[0] in result[i]) and (four[1] in result[i]) and (four[2] in result[i]) and (four[3] in result[i])):
                        nine = list(result[i])
                    else:
                        zero = list(result[i])
                else:
                    six = list(result[i])

        for i in range(0,10): # check unknowns against known values
            if(len(result[i]) == 5): # differentiate between length of 5 for two, three, and five
                if ((one[0] in result[i]) and (one[1] in result[i])):
                    three = list(result[i])
                else:
                    temp = list(result[i])
                    if(((temp[0] == nine[0]) or (temp[0] == nine[1]) or (temp[0] == nine[2]) or (temp[0] == nine[3]) or (temp[0] == nine[4]) or (temp[0] == nine[5])) and ((temp[1] == nine[0]) or (temp[1] == nine[1]) or (temp[1] == nine[2]) or (temp[1] == nine[3]) or (temp[1] == nine[4]) or (temp[1] == nine[5])) and ((temp[2] == nine[0]) or (temp[2] == nine[1]) or (temp[2] == nine[2]) or (temp[2] == nine[3]) or (temp[2] == nine[4]) or (temp[2] == nine[5])) and ((temp[3] == nine[0]) or (temp[3] == nine[1]) or (temp[3] == nine[2]) or (temp[3] == nine[3]) or (temp[3] == nine[4]) or (temp[3] == nine[5])) and ((temp[4] == nine[0]) or (temp[4] == nine[1]) or (temp[4] == nine[2]) or (temp[4] == nine[3]) or (temp[4] == nine[4]) or (temp[4] == nine[5]))):
                        five = list(result[i])
                    else:
                        two = list(result[i])

        zero = sorted(zero)
        one = sorted(one)
        two = sorted(two)
        three = sorted(three)
        four = sorted(four)
        five = sorted(five)
        six = sorted(six)
        seven = sorted(seven)
        eight = sorted(eight)
        nine = sorted(nine)
        
        zero = ''.join(zero)
        one = ''.join(one)
        two = ''.join(two)
        three = ''.join(three)
        four = ''.join(four)
        five = ''.join(five)
        six = ''.join(six)
        seven = ''.join(seven)
        eight = ''.join(eight)
        nine = ''.join(nine)

        print("Zero " + str(zero) + " One " + str(one) + " Two " + str(two) + " Three " + str(three) + " Four " + str(four) + " Five " + str(five) + " Six " + str(six) + " Seven " + str(seven) + " Eight " + str(eight) + " Nine " + str(nine))
        
    
        value = 0

        line = []
        line.append(result[10])
        line.append(result[11])
        line.append(result[12])
        line.append(result[13])
        result = line

        result[0] = sorted(result[0])
        result[1] = sorted(result[1])
        result[2] = sorted(result[2])
        result[3] = sorted(result[3])

        result[0] = ''.join(result[0])
        result[1] = ''.join(result[1])
        result[2] = ''.join(result[2])
        result[3] = ''.join(result[3])

        
        for k in range(0,4):
            if("\n" in result[k]):
                result[k] = str(result[k]).lstrip()

        print(result)

        if(eight != "abcdefg"):
            eight = "abcdefg"

        for i in range(0,4):
            if(result[i] == one):
                value = (value * 10) + 1
            elif(result[i] == two):
                value = (value * 10) + 2
            elif(result[i] == three):
                value = (value * 10) + 3
            elif(result[i] == four):
                value = (value * 10) + 4
            elif(result[i] == five):
                value = (value * 10) + 5
            elif(result[i] == six):
                value = (value * 10) + 6
            elif(result[i] == seven):
                value = (value * 10) + 7
            elif(result[i] == eight):
                value = (value * 10) + 8
            elif(result[i] == nine):
                value = (value * 10) + 9
            elif(result[i] == zero):
                value = (value * 10)
                       
        print(value)

        totalValue += int(value)

print(totalValue)