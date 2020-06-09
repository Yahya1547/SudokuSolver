def check_horizontal(sudoku, i,j) :
    for x in range(9) :
        if x != j and sudoku[i][j] == sudoku[i][x]:
            return False

    return True

def check_vertical(sudoku, i, j) :
    for y in range(9) :
        if y != i and sudoku[i][j] == sudoku[y][j]:
            return False
    
    return True

def check_square(sudoku, i, j) :
    first = [0,1,2]
    second = [3,4,5]
    third = [6,7,8]
    squares = [first, second, third]

    for square in squares :
        if i in square :
            row = square
        if j in square :
            col = square

    for x in row :
        for y in col :
            if x != i or y != j :
                if sudoku[i][j] == sudoku[x][y] :
                    return False
    
    return True

def solve(sudoku) :
    possible = find_empty(sudoku)
    if not possible :
        return True
    else :
        row, col = possible[0], possible[1]
    
    for i in range(1, 10) :
        sudoku[row][col] = i
        ver = check_vertical(sudoku, row, col)
        hor = check_horizontal(sudoku, row, col)
        square = check_square(sudoku, row, col)

        if ver and hor and square :
            if solve(sudoku) :
                return True
        
        sudoku[row][col] = 0
    
    return False
            

def find_empty(sudoku) :
    for i in range(9) :
        for j in range(9) :
            if sudoku[i][j] == 0 :
                return (i,j)
    
    return False
