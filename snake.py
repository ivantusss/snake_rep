# import necessary things

from turtle import *
from random import randint

# making net

tracer(0)
hideturtle()

k      = 50 # turtles size coefficient
x, y   = 14, 10 # net size (cells count)
x0, y0 = -1*x//2, -1*y//2 # new coords sys for simple drawing
x1, y1 = x//2, y//2
setup(x*k +2*k,y*k +2*k)

def net():

    setheading(0)
    penup()

    for a in range(y0, y1 +1):
        setpos(x0*k, a*k)
        pendown()
        forward(x*k)
        penup()

    left(90)
    for b in range(x0, x1 +1):
        setpos(b*k, y0*k)
        pendown()
        forward(y*k)
        penup()

    setpos(x0*k,y0*k)
    pendown()
    pensize(3)
    pencolor('red')
    for i in range(2):
        forward(y*k)
        right(90)
        forward(x*k)
        right(90)

    update()

# mooving directions

def go_up():
    global direction
    if direction != 'down':
        direction = 'up'

def go_down():
    global direction
    if direction != 'up':
        direction = 'down'

def go_right():
    global direction
    if direction != 'left':
        direction = 'right'
    
def go_left():
    global direction
    if direction != 'right':
        direction = 'left'

# apple spawn

def apple_spawn():
    global apple, apple_spawn_req

    if apple_spawn_req is False:
        return apple

    while True:
        apple_x = randint(x0, x1 -1)
        apple_y = randint(y0, y1 -1)
        apple = [apple_x*k, apple_y*k]
        
        if apple not in snake:
            apple_spawn_req = False
            return apple

# snake spawn

def snakes_head():
    global snake, head
    
    if direction == 'up':
        head = [head[0],head[1]+k]

    if direction == 'down':
        head = [head[0],head[1]-k]

    if direction == 'right':
        head = [head[0]+k,head[1]]

    if direction == 'left':
        head = [head[0]-k,head[1]]

    snake.append(head)

def snakes_tail():
    global apple_spawn_req, snake
    
    if head == apple:
        apple_spawn_req = True
    else:
        snake.pop(0)
        
# end of the game

def snakes_bump():

    if head[0] < x0*k or head[0] > x1*k -k:
        return True

    if head[1] < y0*k or head[1] > y1*k -k:
        return True
    
    if head in snake[:-1]:
        return True

    return False

# cell fill

def cell_fill(c_x,c_y, fill_color):
    setheading(0)
    penup()
    setpos(c_x, c_y)
    color('black', fill_color)
    begin_fill()
    for i in range(4):
        forward(k)
        left(90)
    end_fill()

# drawing snake and apple

def snake_and_apple_rendering():
    
    cell_fill(apple[0], apple[1], 'green')
    cell_fill(head[0], head[1], 'brown')
    
    for cell in snake[:-1]:
        cell_fill(cell[0], cell[1], 'red')

# turn on mooving keys

listen()
onkey(go_up, 'Up')
onkey(go_down, 'Down')
onkey(go_right, 'Right')
onkey(go_left, 'Left')

# begin settings

apple           = [-1*k, -1*k]
apple_spawn_req = False
snake           = [[0,0],[k,0]]
head            = snake[-1]
direction       = 'right'

# screen update

def screen_update():

    apple_spawn()
    snakes_head()
    snakes_tail()

    if snakes_bump():
        clear()
        return

    clear()
    net()
    snake_and_apple_rendering()
    update()

    ontimer(screen_update, 150)
    
# game start

screen_update()
done()