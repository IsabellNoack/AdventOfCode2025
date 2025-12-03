sum = 0

with open("day3/input.txt") as file:
    while line := file.readline():
        line = line.strip() # entfernt whitespaces
        maxValue = max(line)
        maxValueIndex = line.index(maxValue)
        lenghtLine = len(line)

        if lenghtLine == maxValueIndex+1:
            popedLine = line[:-1] # entfernt das letzte element der list
            maxValue = max(popedLine) # von der popped line das neue max suchen
            maxValueIndex = line.index(maxValue)

        newLine = line[maxValueIndex +1:]
        secondMaxValue = max(newLine)
        secondMaxValueIndex = line.index(secondMaxValue)
        number = maxValue + secondMaxValue
        # print("number:", number)

        sum = sum + int(number)

print("sum:", sum)