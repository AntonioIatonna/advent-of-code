total = 0

with open('day4Input.txt', 'r') as file:
    
    for line in file:
        pair1, pair2 = line.split(",")
        
        pair1Start, pair1End = pair1.split("-")
        pair2Start, pair2End = pair2.split("-")

        setA = set(i for i in range(int(pair1Start), int(pair1End) + 1))
        setB = set(i for i in range(int(pair2Start), int(pair2End) + 1))

        if((setA.intersection(setB) == setA) or (setA.intersection(setB) == setB)):
            total += 1

    file.close()

    print(total)