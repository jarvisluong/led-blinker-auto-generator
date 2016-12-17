import board
#import play board
board_play=board.board_play
#import mode
mode=board.mode

#previous_obstacle_state
previous_obstacle_display = 0
previous_car_state = int()

#x is starting column,y is the row, z is length of obstacle, m is mode
def obstacle(x,y,z,m):
    output=list()
    for i in range(x,x+z):
        output.append(mode[m])
        output.append(board_play[y,i])
    return '"'+''.join(output) +'"'+ '\n'
