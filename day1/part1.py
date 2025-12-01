dailStart = 50
dailMinimum = 0
dailMaximum = 99
currentNumber = dailStart
countZero = 0 # number how often the dial is pointed at 0

with open("input.txt") as file:
    while line := file.readline(): # for every line in the file
        print("line: ", line.rstrip())

        if (line.startswith("R")) :         # rechts +1
            print("line starts with R")
            number = int(line[1:])

            for i in range(number) :        # für jeden click
                if currentNumber == 99 :
                    currentNumber = 0
                else :
                    currentNumber+=1

        else :                              # links -1
            print("line starts with L")
            number = int(line[1:])

            for i in range(number) :        # für jeden click
                if currentNumber == 0 :
                    currentNumber = 99
                else :
                    currentNumber-=1

        if currentNumber == 0 :
            countZero +=1
        
        print("current Number =", currentNumber)
        print("")
    print("How often the dial pointed at zero: ", countZero)

