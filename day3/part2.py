sum = 0
numberOfDigits = 12
number = ""

with open("day3/input.txt") as file:
    while line := file.readline():
        line = line.strip() # entfernt whitespaces
        print("line:", line)

        for i in reversed(range(numberOfDigits)):
            
            shortLine = line
            if i != 0:
                shortLine = line[:-i]

            # von den digits schauen, welche der max ist!
            maxValue = max(shortLine)
            maxValueIndex = shortLine.index(maxValue)

            number = str(number) + str(maxValue)
            print("number: ", number)

            # alles vorne dran vor der line abschneiden!
            line = line[maxValueIndex +1:]

        sum = sum + int(number)
        number = "" # reset number
        print("")
        
print("sum:", sum)