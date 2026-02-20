import pgzrun
import random

score = 0
apple = Actor("apple")
def draw():
    screen.draw.text(score, 50, 750)
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = random.randint(10, 800)
    apple.y = random.randint(10, 600)
def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        print("Good shot!")
        score += 1
        place_apple()
    else:
        print("You missed!")
        score = 0

place_apple()
pgzrun.go()
