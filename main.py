#!/usr/bin/env python3
import pgzrun
import random
import os

WIDTH = 800
HEIGHT = 600

score = 0
high_score = 0
lives = 3

apple = Actor("apple")


# -------------------------------------------------
# File Handling
# -------------------------------------------------

def get_save_path():
    base_dir = os.path.expanduser("~/.local/share/shoot-the-fruit")
    os.makedirs(base_dir, exist_ok=True)
    return os.path.join(base_dir, "highscore.txt")


def load_high_score():
    global high_score
    path = get_save_path()

    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                high_score = int(f.read())
        except (ValueError, IOError):
            high_score = 0
    else:
        high_score = 0


def save_high_score():
    path = get_save_path()
    with open(path, "w") as f:
        f.write(str(high_score))


# -------------------------------------------------
# Game Logic
# -------------------------------------------------

def place_apple():
    # Keep apple fully inside screen
    apple.x = random.randint(apple.width // 2, WIDTH - apple.width // 2)
    apple.y = random.randint(apple.height // 2, HEIGHT - apple.height // 2)


def reset_game():
    global score, lives
    score = 0
    lives = 3
    place_apple()


# -------------------------------------------------
# Drawing
# -------------------------------------------------

def draw():
    screen.clear()

    screen.draw.text(
        f"Score: {score}",
        (20, 20),
        fontsize=40,
        color="white"
    )

    screen.draw.text(
        f"High Score: {high_score}",
        (20, 70),
        fontsize=35,
        color="yellow"
    )

    screen.draw.text(
        f"Lives: {lives}",
        (20, 115),
        fontsize=35,
        color="red"
    )

    if lives > 0:
        apple.draw()
    else:
        screen.draw.text(
            "GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2 - 40),
            fontsize=80,
            color="red"
        )
        screen.draw.text(
            "Click to Restart",
            center=(WIDTH // 2, HEIGHT // 2 + 40),
            fontsize=40,
            color="white"
        )


# -------------------------------------------------
# Input Handling
# -------------------------------------------------

def on_mouse_down(pos):
    global score, high_score, lives

    if lives <= 0:
        reset_game()
        return

    if apple.collidepoint(pos):
        score += 1
        place_apple()

        if score > high_score:
            high_score = score
            save_high_score()
    else:
        lives -= 1


# -------------------------------------------------
# Start Game
# -------------------------------------------------

load_high_score()
place_apple()
pgzrun.go()