import curses
import time
import random

# Initialize screen
stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
stdscr.nodelay(True)

maxl = curses.LINES
maxc = curses.COLS

# Player position and score
player_x = 0
player_y = 0
score = 0
goal = 100
time_limit = 60  # seconds

# Draw background
def draw_background():
    for y in range(maxl - 1):
        for x in range(maxc - 1):
            if random.random() < 0.03:
                stdscr.addch(y, x, '.')
    stdscr.refresh()

def score_check(player_y, player_x):
    global score
    curr = stdscr.inch(player_y, player_x) & 0xFF 
    if chr(curr) == '.':
        score += 10

def draw_status(remaining):
    stdscr.move(0, 0)
    stdscr.clrtoeol()
    stdscr.addstr(0, 0, f"Score: {score}    Time left: {int(remaining)}s    Goal: {goal}")
    stdscr.refresh()

# Draw player
def draw_player():
    score_check(player_y, player_x)
    stdscr.addch(player_y, player_x, '*')

# Erase player
def erase_player():
    stdscr.addch(player_y, player_x, ' ')

# Initial screen
def init():
    global player_x, player_y
    stdscr.addstr(maxl // 2, maxc // 2 - len("Welcome to my test Game") // 2, "Welcome to my test Game")
    stdscr.refresh()
    time.sleep(1)
    stdscr.clear()

    draw_background()

    # Random player start
    player_y = random.randint(1, maxl - 2)
    player_x = random.randint(1, maxc - 2)
    draw_player()

# Move logic
def move(c):
    global player_x, player_y
    erase_player()

    if c == 'a' and player_x > 0:
        player_x -= 1
    elif c == 'd' and player_x < maxc - 2:
        player_x += 1
    elif c == 'w' and player_y > 1:  # Avoid overwriting status
        player_y -= 1
    elif c == 's' and player_y < maxl - 2:
        player_y += 1

    draw_player()

# Goodbye screen
def bye(message="Good to see you"):
    stdscr.clear()
    stdscr.addstr(maxl // 2, maxc // 2 - len(message) // 2, message)
    stdscr.refresh()
    time.sleep(2)

# --- Run the game ---

init()
playing = True
start_time = time.time()

while playing:
    try:
        current_time = time.time()
        elapsed = current_time - start_time
        remaining = time_limit - elapsed

        # Draw score and time
        draw_status(remaining)

        # Check end conditions
        if score >= goal:
            bye("🎉 You won! Great job!")
            break
        elif remaining <= 0:
            bye("⏰ Time's up! You lost.")
            break

        # Player input
        c = stdscr.getkey()
        if c in 'wasd':
            move(c)
        elif c == 'q':
            playing = False

    except:
        time.sleep(0.05)
        continue

curses.endwin()
