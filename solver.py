
board = [[9, 0, 0, 0, 7, 0, 4, 0, 0,],
         [0, 0, 0, 0, 0, 6, 0, 5, 8,],
         [2, 0, 0, 0, 3, 0, 0, 0, 0,],
         [0, 0, 0, 0, 0, 0, 6, 1, 5,],
         [0, 9, 0, 7, 0, 0, 0, 0, 0,],
         [0, 0, 0, 0, 2, 0, 0, 3, 0,],
         [0, 0, 0, 6, 0, 1, 0, 0, 0,],
         [3, 6, 0, 0, 0, 0, 0, 7, 0,],
         [4, 2, 0, 0, 0, 0, 0, 0, 0,],]


def printBoard():
    print('   0 1 2   3 4 5   6 7 8')
    print(' +-----------------------+')
    i = 0
    for row in board:
        s = str(i) + '| '
        j = 0
        for val in row:
            s += str(val) + ' '
            j += 1
            if j % 3 == 0:
                s += '| '
        print(s)
        i += 1
        if i % 3 == 0 and i != 9:
            print(' |-------+-------+-------|')
    print(' +-----------------------+')
    
    
def blanksRemaining():
    count = 0
    for row in board:
        for val in row:
            if val == 0:
                count += 1
    print(f'{count} blanks remaining')
        

def validAnswers(i, j):
    if board[i][j] == 0:
        answers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
        
        # Check row
        answers = [x for x in answers if x not in board[i]]
        
        # Check column
        col = [row[j] for row in board]
        answers = [x for x in answers if x not in col]
        
        # Check square
        a = i // 3 * 3
        b = j // 3 * 3
        sqr = []
        for x in range(a, a + 3):
            for y in range(b, b + 3):
                sqr.append(board[x][y])
        answers = [x for x in answers if x not in sqr]
        
        return answers
    else:
        return [0,]
        

def solveValid():
    '''Solves cells where only one number is a valid answer'''
    count = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            answers = validAnswers(i, j)
            if len(answers) == 1 and answers[0] != 0:
                print(f'Cell ({i}, {j}) = {answers[0]}')
                board[i][j] = answers[0]
                count += 1
    print(f'{count} cells solved')
    return count


def solveRows():
    '''Solves cells where the cell has the only valid answer in the row'''
    rows = len(board)
    columns = len(board[0])
    count = 0
    
    # Find all valid answers in the row
    for x in range(0, rows):
        all_answers = []
        for y in range(0, columns):
            answers = validAnswers(x, y)
            if answers[0] != 0:
                all_answers.extend(answers)
                
        # find if there are any unique values in this row
        unique_answers = []
        for i in range(1, 10):
            if all_answers.count(i) == 1:
                unique_answers.append(i)
                
        # Find the cells(s) with a unique value and update board
        for unique in unique_answers:
            for y in range(0, columns):
                answers = validAnswers(x, y)
                if unique in answers:
                    board[x][y] = unique
                    count += 1
                    print(f'There is a unique value in cell ({x}, {y}) = {unique}')
    print(f'{count} cells solved')
    return count
                    


def solveSquares():
    '''Solves cells where the cell has the only valid answer in the square'''
    sqr_rows = len(board) // 3
    sqr_cols = len(board[0]) // 3
    
    count = 0
    for sqr_row in range(0, sqr_rows):
        for sqr_col in range(0, sqr_cols):
            
            # Find all valid answers for square
            all_answers = []
            for x in range(sqr_row*3, sqr_row*3 + 3):
                for y in range(sqr_col*3, sqr_col*3 + 3):
                    answers = validAnswers(x, y)
                    if answers[0] != 0:
                        all_answers.extend(answers)
                        
            # Find if there are any unique value in this square
            unique_answers = []
            for i in range(1, 10):
                if all_answers.count(i) == 1:
                    unique_answers.append(i)
                    
            # Find the cell(s) with a unique value(s) and update board
            for unique in unique_answers:
                for x in range(sqr_row*3, sqr_row*3 + 3):
                    for y in range(sqr_col*3, sqr_col*3 + 3):
                        answers = validAnswers(x, y)
                        if unique in answers:
                            board[x][y] = unique
                            count += 1
                            print(f'There is a unique value in cell ({x}, {y}) = {unique}')
    print(f'{count} cells solved')
    return count



                
                
            


def solver():
    count = -1
    while count != 0:
        count = solveValid()
        
    count = -1
    while count != 0:
        count = solveRows()
    
    count = -1
    while count != 0:
        count = solveSquares()


if __name__ == '__main__':
    blanksRemaining()
    printBoard()

    solver()
    blanksRemaining()
    printBoard()
    
    solver()
    blanksRemaining()
    printBoard()
    
    solver()
    blanksRemaining()
    printBoard()
