from random import*
from turtle import*
from freegames import vector
bird = vector(0,0)
enemys = []
def tap(x,y):
    l = vector(0, 30) 
    bird.move(l)
def inside(point):
    return -200<point.x<200 and -200<point.y<200

def draw(alive):
    clear()
    goto(bird.x,bird.y)
    if alive:
        dot(20,'green')
    else:
        dot(20,'red')
    for ball in enemys:
        goto(ball.x,ball.y)
        dot(15,'black')
    update()
def move():
    bird.y-=5
    for ball in enemys:
        ball.x-=3
    if randrange(10)==0:
        y = randrange(-199,199)
        e = vector(199,y)
        enemys.append(e)
    while (len(enemys)>0 and not inside(enemys[0])):
        enemys.pop(0)
    if not inside(bird):
        draw(False)
        return
    for ball in enemys:
        if abs(ball-bird)<15:
            draw(False)
            return
    draw(True)
    ontimer(move,50)
setup(420,420,370,0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()