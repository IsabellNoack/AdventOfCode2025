matrix = []
character = ''
countNeightbours = 0
sumForkliftSpace = 0
didRemovePaperRoll = True

def isWhat(i,j):
    if i > len(matrix)-1 or i < 0:
        return 'not existing'
    elif j > len(matrix[i])-1 or j < 0:
        return 'not existing'
    elif matrix[i][j] == '.':
        return 'empty'
    elif matrix[i][j] == '@':
        return 'paper roll'

with open("day4/input.txt") as file:
    matrix = file.read().split('\n')
    
    for i in range(len(matrix)):
        matrix[i] = list(matrix[i]) # macht aus string nen array aus charactern

while didRemovePaperRoll == True:
    
    didRemovePaperRoll = False
    
    for i in range(len(matrix)): # for every line
        # print("i:", i)

        for j in range(len(matrix[i])): # for every char

            character = isWhat(i,j)
            countNeightbours = 0
            if character == 'paper roll':

                top = isWhat(i-1,j)
                topLeft = isWhat(i-1,j-1)
                topRight = isWhat(i-1,j+1)
                left = isWhat(i,j-1)
                right = isWhat(i,j+1)
                button = isWhat(i+1,j)
                buttonLeft = isWhat(i+1,j-1)
                buttonRight = isWhat(i+1,j+1)

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

            if countNeightbours <= 3:  # Paper roll can be removed!
                # print("countNeightbours",countNeightbours)

                sumForkliftSpace+=1
                matrix[i][j] = '.'
                didRemovePaperRoll = True
     
print("sumForkliftSpace: ", sumForkliftSpace)