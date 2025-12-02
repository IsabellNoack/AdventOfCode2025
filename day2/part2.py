import math
from numberValidation import numberValidation

file = open("day2/input.txt")
data = file.read().split(',')
numberOfInvalidIDs = 0
sumInvalidIDs = 0
n = 0
m = 0
numberIsValid = True

for i in data :                                     # Beispiel 11-22
    i = i.split('-')                                # 11, 22
    startNumber = int(i[0])                         # 11
    endNumber = int(i[1])                           # 22
    
    for x in range(startNumber,endNumber+1) :       # range(11, 22) => [11,12,13,14,15,16,17,18,19,20,21]
        # print("x", x)
        x = str(x)                                  # mit x als string weiter machen

        numberIsValid = numberValidation(x)             # true or false
        if numberIsValid == False :

            sumInvalidIDs = sumInvalidIDs + int(x)
            numberOfInvalidIDs+=1
            # print(x + " is invalid ID, SUM: " + str(sumInvalidIDs))

print("")
print("Counter Invalid IDs:", numberOfInvalidIDs)
print("Sum Invalid IDs:", sumInvalidIDs)