matrix = []
binIchSelberEineRolle = ''
countNeightbours = 0
sumForkliftSpace = 0

def isWhat(i,j):
    if i > len(matrix)-1 or i < 0:
        return  False
    elif j > len(matrix[i])-1 or j < 0:
        return False
    
    return (matrix[i][j] == '@')

with open("day4/input.txt") as file:
    matrix = file.read().split('\n')

for i in range(len(matrix)): # for every line
    # print("i:", i)

    for j in range(len(matrix[i])): # for every char

        binIchSelberEineRolle = isWhat(i,j)
        countNeightbours = 0
        if matrix[i][j] != '@':
            continue

# [i-1][j-1]    [i-1][j]    [i-1][j+1]
# [i]  [j-1]    [i]  [j]    [i]  [j+1]
# [i+1][j-1]    [i+1][j]    [i+1][j+1]

        for ii in range(i-1, i+2):
            for jj in range(j-1, j+2):
                if ii == i and jj == j: # wenn wir wir selbst sind nichts machen
                    continue
                if isWhat(ii, jj):
                    countNeightbours += 1

        if countNeightbours <= 3:
            print("countNeightbours",countNeightbours)

            sumForkliftSpace+=1
            print("sumForkliftSpace",sumForkliftSpace)
            print("x on", i , j)
     
# print(matrix[0][0])
print("sumForkliftSpace: ", sumForkliftSpace)