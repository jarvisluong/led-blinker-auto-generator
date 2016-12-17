import board
# board area for numbers
board_numbers = board.board_numbers
# mode on and off for numbers
mode=board.mode

#previous number status
previous = [0,0]

def zero(x):
    output=list()
    global previous
    if previous[x]:
        output.append(mode['off'])
        output.append(str(board_numbers[x][2,1]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][3,0]))
        return '"'+''.join(output) +'"' + '\n'
    for i in range(5):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,0]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,2]))
    output.append(str(board_numbers[x][0,1]))
    output.append(str(board_numbers[x][4,1]))
    previous[x]=1
    return '"'+''.join(output) +'"' + '\n'

def one(x): # x cannot be greater than 1, x is the board and m is mode on or off
    output=list()
    global previous
    if previous[x]:
        for i in range(5):
            output.append(mode['off'])
            output.append(str(board_numbers[x][i,0]))
            output.append(mode['off'])
            output.append(str(board_numbers[x][i,1]))
        return '"'+''.join(output) +'"'+ '\n'
    for i in range(5):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,2]))
    previous[x] = 1
    return '"'+''.join(output) +'"' + '\n'

def two(x):
    output=list()
    global previous
    if previous[x]:
        output.append(mode['off'])
        output.append(str(board_numbers[x][3,2]))
        for i in range(0,5,2):
            output.append(mode['on'])
            output.append(str(board_numbers[x][i,0]))
            output.append(mode['on'])
            output.append(str(board_numbers[x][i,1]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][3,0]))
        return '"'+''.join(output) +'"' + '\n'
    for i in range(0,5,2):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,0]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,1]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,2]))
    output.append(mode['on'])
    output.append(str(board_numbers[x][3,0]))
    output.append(mode['on'])
    output.append(str(board_numbers[x][1,2]))
    previous[x]=1
    return '"'+''.join(output) +'"'+ '\n'

def three(x):
    output=list()
    global previous
    if previous[x]:
        output.append(mode['off'])
        output.append(str(board_numbers[x][3,0]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][3,2]))
        return '"'+''.join(output) +'"'+ '\n'
    for i in range(5):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,2]))
    for i in range(0,5,2):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,0]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,1]))
    previous[x]=1
    return '"'+''.join(output) +'"' + '\n'

def four(x):
    output=list()
    global previous
    if previous[x]:
        output.append(mode['off'])
        output.append(str(board_numbers[x][0,1]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][1,0]))
        output.append(mode['off'])
        output.append(str(board_numbers[x][4,1]))
        output.append(mode['off'])
        output.append(str(board_numbers[x][4,0]))
        return '"'+''.join(output) +'"' + '\n'
    for i in range(5):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,2]))
    for i in range(3):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,0]))
    output.append(mode['on'])
    output.append(str(board_numbers[x][2,1]))
    previous[x]=1
    return '"'+''.join(output) +'"' + '\n'

def five(x):
    output=list()
    global previous
    if previous[x]:
        output.append(mode['off'])
        output.append(str(board_numbers[x][1,2]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][0,1]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][4,0]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][4,1]))
        return '"'+''.join(output) +'"' + '\n'
    for i in range(0,5,2):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,0]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,1]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,2]))
    output.append(mode['on'])
    output.append(str(board_numbers[x][1,0]))
    output.append(mode['on'])
    output.append(str(board_numbers[x][3,2]))
    previous[x]=1
    return '"'+''.join(output) +'"' + '\n'

def six(x):
    output=list()
    global previous
    if previous[x]:
        output.append(mode['on'])
        output.append(str(board_numbers[x][3,0]))
        return '"'+''.join(output) +'"' + '\n'
    for i in range(0,5,2):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,0]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,1]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,2]))
    output.append(mode['on'])
    output.append(str(board_numbers[x][1,0]))
    output.append(mode['on'])
    output.append(str(board_numbers[x][3,2]))
    output.append(mode['on'])
    output.append(str(board_numbers[x][3,0]))
    previous[x]=1
    return '"'+''.join(output) +'"' + '\n'

def seven(x):
    output=list()
    global previous
    if previous[x]:
        for i in range(1,5):
            output.append(mode['off'])
            output.append(str(board_numbers[x][i,0]))
        output.append(mode['off'])
        output.append(str(board_numbers[x][2,1]))
        output.append(mode['off'])
        output.append(str(board_numbers[x][4,1]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][1,2]))
        return '"'+''.join(output) +'"' + '\n'
    for i in range(5):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,2]))
    output.append(mode['on'])
    output.append(str(board_numbers[x][0,0]))
    output.append(mode['on'])
    output.append(str(board_numbers[x][0,1]))
    previous[x] = 1
    return '"'+''.join(output) +'"' + '\n'

def eight(x):
    output=list()
    global previous
    if previous[x]:
        for i in range(1,5):
            output.append(mode['on'])
            output.append(str(board_numbers[x][i,0]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][2,1]))
        output.append(mode['on'])
        output.append(str(board_numbers[x][4,1]))
        return '"'+''.join(output) +'"' + '\n'
    for i in range(5):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,2]))
    for i in range(5):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,0]))
    for i in range(0,5,2):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,1]))
    previous[x] = 1
    return '"'+''.join(output) +'"' + '\n'

def nine(x):
    output=list()
    global previous
    if previous[x]:
        output.append(mode['off'])
        output.append(str(board_numbers[x][3,0]))
        return '"'+''.join(output) +'"' + '\n'
    for i in range(5):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,2]))
    for i in range(0,5,2):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,1]))
    for i in range(3):
        output.append(mode['on'])
        output.append(str(board_numbers[x][i,0]))
    output.append(mode['on'])
    output.append(str(board_numbers[x][4,0]))
    previous[x] = 1
    return '"'+''.join(output) +'"' + '\n'
