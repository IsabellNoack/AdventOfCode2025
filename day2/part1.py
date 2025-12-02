import math

file = open("day2/input.txt")
data = file.read().split(',')
numberOfInvalidIDs = 0
sumInvalidIDs = 0

for i in data :                                     # Beispiel 11-22
    i = i.split('-')                                # 11, 22
    startNumber = int(i[0])                         # 11
    endNumber = int(i[1])                           # 22
    
    for x in range(startNumber,endNumber+1) :       # range(11, 22) => [11,12,13,14,15,16,17,18,19,20,21]
        # print(x)
        x = str(x)                                  # mit x als string weiter machen
        split = math.ceil(len(x)/2)                 # string länge halbieren und aufruden(mit math.ceil)

        firstHalf = x[:split]
        secondHalf = x[split:]

        if firstHalf == secondHalf :
            sumInvalidIDs = sumInvalidIDs + int(x)
            numberOfInvalidIDs+=1
            print(x + " is invalid ID, SUM: " + str(sumInvalidIDs))

print("")
print("Counter Invalid IDs:", numberOfInvalidIDs)
print("Sum Invalid IDs:", sumInvalidIDs)