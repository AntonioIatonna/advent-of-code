with open('day6Input.txt', 'r') as file:
    
    fish = file.read().split(",")
    fish = [int(numeric_string) for numeric_string in fish]

    for days in range(0, 80):
        for i in range(0, len(fish)):
            fish[i] -= 1
            if(fish[i] < 0):
                fish[i] = 6
                fish.append(8)
            
    print("After " + str(days + 1) + " days, there are " + str(len(fish)) + " fish.")