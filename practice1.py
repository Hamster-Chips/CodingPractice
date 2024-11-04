'''
Imagine a black and white image and represts by pixel, pixels are black or white

2d Array
0, 1
1 -> Black
0 -> White

remove all black pixel that are not connected to the boarded of the image
- up/down/left/right
- No diagonal

'''

def removeIsland(matrix):
    
    '''
    Do a nested loop to go through the matrix
    Check the first elem if 1 or not
    Check the 2nd elem if there is a 1 or not
        - If there is a 1
            - Look if the first elem was a 1
                - if first elem is a 1 
                    - Store it in a 'hold' variable <- index
                - else
                    - Store it in the 'delete' variable  <- index
    '''

    hold = []
    delete = []
    boarderHead = False
    boarderTail = False
    for i, row in enumerate(matrix):

        if matrix[i][0] == 1:
            hold.append(matrix[i][0])
            boarderHead = True
        if matrix[i - 1][0] == 1:
            hold.append(matrix[i][-1])
            boarderTail = True

        for j, elem in enumerate(row):
            if matrix[i][j] == 1:
                break
                
        
        hold = []
        boarder = False

    return []

def main():
    print("Hello world")

    matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
    ]

    removeIsland(matrix)

if __name__ == "__main__":
    main()