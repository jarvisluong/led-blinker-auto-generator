from obstacle import obstacle
from car_transition_2 import car
from number_display import zero,one,two,three,four,five,six,seven,eight,nine
from random import randint
#open the output file
output = open('animaatio.h','w')

#list of obstacles
obstacles = {1:[2,4],2:[0,3],3:[1,5],4:[0,3],5:[2,4],6:[1,3],7:[2,5],8:[1,4],
             9:[0,3],10:[4,2]}
def wait():
    output.write('"w0060"\n')

def obstacle_moving(x,n):
    output.write(obstacle(obstacles[x][0],n-1,obstacles[x][1],'off'))
    output.write(obstacle(obstacles[x][0],n,obstacles[x][1],'on'))

def obstacle_on(x):
    output.write(obstacle(obstacles[x][0],0,obstacles[x][1],'on'))

def obstacle_off(x):
    output.write(obstacle(obstacles[x][0],8,obstacles[x][1],'off'))

def car_move(x):
    output.write(car(x))

def cycle():
    obstacle_on(1)
    wait()
    obstacle_moving(1,1)
    wait()
    obstacle_moving(1,2)
    wait()
    obstacle_moving(1,3)
    wait()

    #====== THE LOGIC BEGINS !!!!! ===============
    obstacle_moving(1,4)
    wait()
    obstacle_moving(1,5)
    obstacle_on(2)
    wait()
    obstacle_moving(1,6)
    obstacle_moving(2,1)
    car_move(2)
    wait()
    obstacle_moving(1,7)
    obstacle_moving(2,2)
    car_move(1)
    wait()
    obstacle_moving(1,8)
    obstacle_moving(2,3)
    wait()
    obstacle_off(1)
    output.write(one(1))
    obstacle_moving(2,4)
    obstacle_on(3)
    wait()
    obstacle_moving(2,5)
    obstacle_moving(3,1)
    wait()
    obstacle_moving(2,6)
    obstacle_moving(3,2)
    car_move(2)
    wait()
    obstacle_moving(2,7)
    obstacle_moving(3,3)
    car_move(3)
    wait()
    obstacle_moving(2,8)
    obstacle_moving(3,4)
    obstacle_on(4)
    car_move(4)
    wait()
    obstacle_off(2)
    output.write(two(1))
    obstacle_moving(3,5)
    obstacle_moving(4,1)
    car_move(3)
    wait()
    obstacle_moving(3,6)
    obstacle_moving(4,2)
    car_move(2)
    wait()
    obstacle_moving(3,7)
    obstacle_moving(4,3)
    car_move(1)
    wait()
    obstacle_moving(3,8)
    obstacle_moving(4,4)
    car_move(0)
    wait()
    obstacle_off(3)
    output.write(three(1))
    obstacle_moving(4,5)
    obstacle_on(5)
    car_move(1)
    wait()
    obstacle_moving(4,6)
    obstacle_moving(5,1)
    car_move(2)
    wait()
    obstacle_moving(4,7)
    obstacle_moving(5,2)
    car_move(3)
    wait()
    obstacle_moving(4,8)
    obstacle_moving(5,3)
    car_move(4)
    wait()
    obstacle_off(4)
    output.write(four(1))
    obstacle_moving(5,4)
    wait()
    obstacle_moving(5,5)
    car_move(5)
    wait()
    obstacle_moving(5,6)
    obstacle_on(6)
    car_move(6)
    wait()
    obstacle_moving(5,7)
    obstacle_moving(6,1)
    wait()
    obstacle_moving(5,8)
    obstacle_moving(6,2)
    wait()
    obstacle_off(5)
    output.write(five(1))
    obstacle_moving(6,3)
    wait()
    obstacle_on(7)
    obstacle_moving(6,4)
    wait()
    obstacle_moving(6,5)
    obstacle_moving(7,1)
    wait()
    obstacle_moving(6,6)
    obstacle_moving(7,2)
    obstacle_on(8)
    wait()
    obstacle_moving(6,7)
    obstacle_moving(7,3)
    obstacle_moving(8,1)
    wait()
    obstacle_moving(6,8)
    obstacle_moving(7,4)
    obstacle_moving(8,2)
    wait()
    obstacle_off(6)
    output.write(six(1))
    car_move(5)
    obstacle_moving(7,5)
    obstacle_moving(8,3)
    wait()
    car_move(4)
    obstacle_moving(7,6)
    obstacle_moving(8,4)
    obstacle_on(9)
    wait()
    car_move(3)
    obstacle_moving(7,7)
    obstacle_moving(8,5)
    obstacle_moving(9,1)
    wait()
    car_move(2)
    obstacle_moving(7,8)
    obstacle_moving(8,6)
    obstacle_moving(9,2)
    wait()
    car_move(1)
    obstacle_moving(8,7)
    obstacle_off(7)
    obstacle_moving(9,3)
    output.write(seven(1))
    obstacle_on(10)
    wait()
    car_move(0)
    obstacle_moving(8,8)
    obstacle_moving(9,4)
    obstacle_moving(10,1)
    wait()
    car_move(1)
    obstacle_off(8)
    obstacle_moving(9,5)
    output.write(eight(1))
    obstacle_moving(10,2)
    wait()
    car_move(2)
    obstacle_moving(9,6)
    obstacle_moving(10,3)
    wait()
    obstacle_moving(9,7)
    car_move(3)
    obstacle_moving(10,4)
    wait()
    obstacle_moving(9,8)
    car_move(4)
    obstacle_moving(10,5)
    wait()
    obstacle_off(9)
    output.write(nine(1))
    obstacle_moving(10,6)
    wait()
    obstacle_moving(10,7)
    car_move(3)
    wait()
    obstacle_moving(10,8)
    wait()
    obstacle_off(10)
    output.write(zero(1))


#====== FIRST FRAME OF THE GAME ==============
#display two zeros
output.write(zero(0))
output.write(zero(1))

#the car is on the middle
car_move(3)

cycle()
output.write(one(0))
output.write('"w0060"'+'\n')

#close the output file
output.close()
