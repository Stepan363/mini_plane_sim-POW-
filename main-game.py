import pgzrun
import pygame
import random
from random import randint
import time
WIDTH = 1350
end = 0
t0 = time.time()
i = 0
na = []
import pygame as pg
HEIGHT = 600
plane2 = Actor("plane")
bullet = Actor("bullet")
which_one = 0
picker = 0
flight_attemped = 0
is_flight_attemped = "False"
win = False
plane = Actor("plane")
bullet.pos = -1000,-1000
ax,ay=(random.randint(1340,1350),random.randint(0,600))
tree = Actor("hal_tree")
plane_angle = 0
plane.pos = WIDTH / 2, HEIGHT - 50
tree.pos = WIDTH - 100, HEIGHT - 50
plane_exploded = Actor("plane_exploded")
plane_exploded.pos = plane.pos = WIDTH / 2, HEIGHT - 50
speed = 0
altitude = 0
game_over = False

def is_developer():
    if keyboard.M:
        global flight_attemped
        flight_attemped = 500000

        

def explosion_animation():
    if game_over == True:
        global speed, ax,ay,i
        global plane_angle
        global altitude
        global flight_attemped
        global is_flight_attemped
        speed = 0
        ax,ay=(random.randint(1340,1350),random.randint(0,600))
        i = 0
        plane_angle = 0
        altitude = 0 
        plane_exploded.draw()
        screen.draw.text("YOU CRASHED, PRESS Q TO RESTART", (WIDTH / 2, HEIGHT / 2.5), color="red")
        plane.pos = WIDTH / 2, HEIGHT - 50
        flight_attemped = 0 
        plane_exploded.pos = plane.pos = WIDTH/5 + random.randint(-500,1000), HEIGHT - 50 + random.randint(1,25)
        plane_exploded.draw()
        plane_exploded.pos = plane.pos = WIDTH / 2 - random.randint(1,25), HEIGHT - 50 + random.randint(1,25)
        is_flight_attemped = "False"
def won():
    global altitude
    global is_flight_attemped
    global plane_angle
    global flight_attemped
    global speed, ax,ay,i
    if win == True:
        altitude = 0
        ax,ay=(random.randint(1340,1350),random.randint(0,600))
        i = 0
        plane_angle = 0
        screen.draw.text("SUCCESFULLY PLANE LANDED! PRESS Q TO RESTART", (300, 300), color="green")
        plane.pos = WIDTH / 2, HEIGHT - 50
        flight_attemped = 0
        speed = speed / 2
        is_flight_attemped = "False"


        
def draw_txt():
    screen.draw.text("ALTITUDE", (350, 150), color="black")
    screen.draw.text("SPEED", (360, 140), color="black")

def music_picker_randomizer():
    which_one = random.randint(1,4)
    if which_one == 1:
        music.play("breeze")
    if which_one == 2:
        music.play("first")
    if which_one == 3:
        music.play("time")
    if which_one == 4:
        music.play("tatistical")
music_picker_randomizer()

        
def draw():
    
    global plane_angle, plane, plane_exploded, speed, game_over, altitude, a,b, plane2, bullet
    plane_exploded.draw()
    screen.blit("background", (0, 0))
    plane.draw()
    tree.draw()
    bullet.draw()
    plane2.draw()
    plane.pos = random.randint(1340,1350),random.randint(0,600)
    if keyboard.space:
        screen.draw.text("POW!!!!: " + str(na), (WIDTH/2, HEIGHT/2), color="red")
    if speed < 0:
        
        screen.draw.text("STALL!STALL!STALL!STALL!STALL!STALL!STALL" + str(speed),(675,300), color="red")
    screen.draw.text("Altitude: " + str(altitude), (WIDTH / 2, HEIGHT - 125), color="brown")
    if speed < 2000:
        screen.draw.text("Speed: " + str(speed), (0, 25), color="blue")
    elif speed >= 2000 and speed <= 3000:
        screen.draw.text("Speed: " + str(speed), (0, 25), color="purple")
    else:
        screen.draw.text("Speed: " + str(speed), (0, 25), color="red")
    if plane_angle > 20 or plane_angle < -20:
        screen.draw.text("Plane_angle: " + str(plane_angle), (0, 45), color="red")  
    elif plane_angle > 0 and plane_angle <= 20 or plane_angle < 0 and plane_angle >= -20:
        screen.draw.text("Plane_angle: " + str(plane_angle), (0, 45), color="orange")
    else:
        screen.draw.text("Plane_angle: " + str(plane_angle), (0, 45), color="green")
    if is_flight_attemped == "False":
        screen.draw.text("Is ready to land: " + str(is_flight_attemped), (0, 65), color="orange")
    else:
        screen.draw.text("Is ready to land: " + str(is_flight_attemped), (0, 65), color="green")
    if speed > 0:
        tree.pos = tree.x - speed / 10, HEIGHT - 50
    if altitude > 0:
        tree.pos = tree.x, tree.y + altitude
    if altitude == 0 and plane_angle < -5 or speed < -0 and altitude < 0 or altitude < -2:
        game_over = True
    if speed <= 0 and altitude > 0:
        altitude -= plane_angle
    #if speed < 0:
    #    speed == 0
    if keyboard.E:
        quit()
    if plane_angle > 20:
        plane = Actor("plane_40_degrees")
        plane.pos = WIDTH / 2, HEIGHT - 50
    if plane_angle > 0 and plane_angle < 21:
        plane = Actor("plane_20_degrees")
        plane.pos = WIDTH / 2, HEIGHT - 50
    if plane_angle == 0:
        plane = Actor("plane")
        plane.pos = WIDTH / 2, HEIGHT - 50
    if plane_angle < 0 and plane_angle > - 21:
        plane = Actor("plane_20_degr_tilted")
        plane.pos = WIDTH / 2, HEIGHT - 50

    if plane_angle < -20 and plane_angle > - 40:
        plane = Actor("plane_40_degr_tilted")
        plane.pos = WIDTH / 2, HEIGHT - 50
    explosion_animation()
    won()
def tree_change():
    
    global picker
    picker = random.randint(1,4)
    if picker == 1:
        tree = Actor("tree")
    if picker == 2:
        tree = Actor("chr_tree")
    if picker == 3:
        tree = Actor("hal_tree")
    if picker == 4:
        tree = Actor("troll")
    
def update():
    global altitude, t0,i, plane2, ax,ay,end
    global speed
    global plane
    global win
    global is_flight_attemped
    global flight_attemped
    global plane_angle
    global game_over
    is_developer()
    if tree.x < 20:
        tree.pos = WIDTH - 100, tree.y
    
    if keyboard.down and speed != 0 and speed > 60:
        if altitude != 0 or altitude != 1:
            altitude += 0.1
        speed -= 3
        if plane_angle >= -46 and plane_angle < 45:
            plane_angle += 0.5
    if plane_angle > 0:
        flight_attemped += altitude
    if keyboard.up and speed != 0:
        if altitude >= 0 and altitude != 0:
            altitude -= 0.1
            speed += 0.1
        if plane_angle <= 46 and plane_angle >= -45:
            plane_angle -= 0.5
    if keyboard.right:
        speed += 6
    if speed != 0:
        if keyboard.left and speed != 0:
            speed -= 6
    if keyboard.space:
        bullet.pos = plane2.pos
        
    else:
        for z in range(10):
            bullet.pos = -1000,-1000
    
    if keyboard.Q and game_over == True or keyboard.Q and win == True:
        game_over = False
        win = False
        plane_exploded.pos = plane.pos = WIDTH / 2, HEIGHT - 50

        plane.pos = WIDTH / 2, HEIGHT - 50
        tree.pos = WIDTH - 100, HEIGHT - 50
    speed = round(speed)
    altitude = round(altitude)
    if plane_angle > 0:
        speed -= plane_angle/2
        altitude += plane_angle/2
    if plane_angle < 0:
        speed += abs(plane_angle)/2
        altitude += plane_angle/2
    
    if speed > 1500:
        plane.pos = plane.x + random.randint(1,5), plane.y - random.randint(1,5)
    if plane_angle > 0 and plane.y >= 170 and plane.y <= 550:
        plane.pos = plane.x, plane.y - plane_angle*20
    
    if flight_attemped >= 500000:
        is_flight_attemped = "Ready"
    if plane_angle <= 0 and plane_angle >= -6 and altitude < 0 and altitude > -10 and flight_attemped >= 500000 and speed < 2000:
        win = True




    #enemy_birds_code:
        
    
    bx,by=(int(plane.x), int(plane.y))
    

    steps_number = max( abs(bx-ax), abs(by-ay) )

    #print(int(ax + stepx), int(ay + stepy))
    
    dx, dy = (bx - ax, by - ay)
    stepx, stepy = (dx / 25., dy / 25.)
    
    t1 = time.time()
    dt = t1 - t0
    #print(dt)
    if dt >= 0.1:
        t0 = t1
        #print("plane.pos:", plane.pos)
        #print("plane2.pos:",plane2.pos)
        #print(plane2.pos == plane.pos)
        plane2.pos = int(ax + stepx*i), int(ay + stepy*i)
        i+= 1
        dt = t1 - t0
        
    if plane2.pos == plane.pos:
        game_over = True

    
    if bullet.colliderect(plane2):
       i = 0
       ax,ay=(random.randint(1340,1350),random.randint(0,600))
    

pgzrun.go()

'''

'''


#tada!z 