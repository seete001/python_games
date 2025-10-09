import random
import curses
from time import sleep

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
stdscr.nodelay(False)
maxl = curses.LINES
maxc = curses.COLS

def menu():
    stdscr.clear()
    stdscr.addstr   (maxl // 2, maxc // 2 - len("Ready to guess a number ...") // 2, "Ready to guess a number ...")
    stdscr.refresh()
    sleep(2)
    stdscr.getkey()

def generate():
    return str(random.randint(1,10))


def guess(target):

    stdscr.clear()
    stdscr.addstr(maxl//2, maxc // 2 - len("Guess a number (1-9)") // 2, "Guess a number (1-9)")
    stdscr.refresh()

    while True:
        try:
            key = stdscr.getch()
            if key == -1:
                continue
            if chr(key) == 'q':
                exit()
            if chr(key).isdigit():
                if chr(key) == target:
                    return True
                else:
                    return False
        except:
            continue

def status(count):
    stdscr.clear()
    msg = f"you won the game with {count} chances"
    stdscr.addstr(maxl // 2, maxc // 2- len(msg) // 2, msg)
    stdscr.refresh()
    sleep(1.5)
    


#-------------------------------------------------------------    
menu()
win = False
target = generate()
count = 1
while not win:
    if guess(target):
        status(count)
        win = True
    else:
        stdscr.clear()
        stdscr.addstr(maxl // 2,maxc // 2-  len("not a chance") // 2,"not a chance")
        stdscr.refresh()
        count += 1
        sleep(1.5)

curses.endwin()
