matrix = []
character = ''
countNeightbours = 0
sumForkliftSpace = 0

def isWhat(i,j):
    if i > len(matrix)-1 or i < 0:
        return 'not existing'
    elif j > len(matrix[i])-1 or j < 0:
        return 'not existing'
    elif matrix[i][j] == '.':
        return 'empty'
    elif matrix[i][j] == '@':
        # countNeightbours+=1
        return 'paper roll'
    
with open("day4/input.txt") as file:
    matrix = file.read().split('\n')

for i in range(len(matrix)): # for every line
    # print("i:", i)

    for j in range(len(matrix[i])): # for every char

        character = isWhat(i,j)
        countNeightbours = 0
        if character == 'paper roll':

            

# [i-1][j-1]    [i-1][j]    [i-1][j+1]
# [i][j-1]      [i][j]      [i][j+1]
# [i+1][j-1]    [i+1][j]    [i+1][j+1]

            top = isWhat(i-1,j)
            topLeft = isWhat(i-1,j-1)
            topRight = isWhat(i-1,j+1)
            left = isWhat(i,j-1)
            right = isWhat(i,j+1)
            button = isWhat(i+1,j)
            buttonLeft = isWhat(i+1,j-1)
            buttonRight = isWhat(i+1,j+1)

            # print("------------------------")
            # print(topLeft, top, topRight)
            # print(left, character, right)
            # print(buttonLeft, button, buttonRight)
            # print("------------------------")

            if top == 'paper roll':
                countNeightbours+=1
            if topLeft == 'paper roll':
                countNeightbours+=1
            if topRight == 'paper roll':
                countNeightbours+=1
            if left == 'paper roll':
                countNeightbours+=1
            if right == 'paper roll':
                countNeightbours+=1
            if button == 'paper roll':
                countNeightbours+=1
            if buttonLeft == 'paper roll':
                countNeightbours+=1
            if buttonRight == 'paper roll':
                countNeightbours+=1
        else:
            countNeightbours = 999

        if countNeightbours <= 3:
            print("countNeightbours",countNeightbours)

            sumForkliftSpace+=1
            print("sumForkliftSpace",sumForkliftSpace)
            print("x on", i , j)
     
# print(matrix[0][0])
print("sumForkliftSpace: ", sumForkliftSpace)