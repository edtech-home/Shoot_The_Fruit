import pgzrun
import random
import os

score = 0
high_score = 0
apple = Actor("apple")

# Load high score from file
def load_high_score():
    global high_score
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as f:
            high_score = int(f.read())
    else:
        high_score = 0

# Save high score to file
def save_high_score():
    with open("highscore.txt", "w") as f:
        f.write(str(high_score))

def draw():
    screen.clear()
    
    screen.draw.text(
        "Score: " + str(score),
        (50, 50),
        fontsize=50,
        color="white",
    )
    
    screen.draw.text(
        "High Score: " + str(high_score),
        (50, 110),
        fontsize=40,
        color="yellow",
    )
    
    apple.draw()

def place_apple():
    apple.x = random.randint(10, 800)
    apple.y = random.randint(10, 600)

def on_mouse_down(pos):
    global score, high_score
    
    if apple.collidepoint(pos):
        print("Good shot!")
        score += 1
        place_apple()
        
        # Update high score
        if score > high_score:
            high_score = score
            save_high_score()
    else:
        print("You missed!")
        score = 0

# Load high score when game starts
load_high_score()
place_apple()
pgzrun.go()