import board
#display the playboard
board_play = board.board_play

#mode in playboard
mode=board.mode

#previous_car_state
previous_car_display = 0
previous_car_state = int()

def car(x):
    output=list()
    global previous_car_display
    global previous_car_state
    if previous_car_display:
        output.append(mode['off'])
        output.append(str(board_play[9,previous_car_state]))
        output.append(mode['off'])
        output.append(str(board_play[10,previous_car_state]))
        output.append(mode['on'])
        output.append(str(board_play[9,x]))
        output.append(mode['on'])
        output.append(str(board_play[10,x]))
        previous_car_state=x
        return '"'+''.join(output) +'"' + '\n'
    for i in range(9,11):
        output.append(mode['on'])
        output.append(str(board_play[i,x]))
    previous_car_state=x
    previous_car_display=1
    return '"'+''.join(output) +'"'+ '\n'
