import pygame as pg,sys
from pygame.locals import *
import time
import random

# initialise global variables
XO = 'x'
START = XO
WINNER = None
DRAW = False
WIDTH = 600
HEIGHT = 600
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
GREEN = (150, 255, 150)
BLUEGRAY = (92, 145, 191)
RED = (237, 28, 36)
GREENGRAY = (75, 163, 147)
LIGHTGREENGRAY = (171, 237, 225)
GRAY = (133, 132, 143)
LIGHTGRAY = (195, 194, 204)

# Naughts & Crosses 3x3 board
BOARD = [[None]*3,[None]*3,[None]*3]

# initialising pygame window
pg.init()
fps = 30 # frames per second
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT+100), 0, 32)
pg.display.set_caption("Noughts & Crosses")

# loading the images
opening = pg.image.load('StartUpImage.png')
x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')

# resising images
x_img = pg.transform.scale(x_img, (150,150))
o_img = pg.transform.scale(o_img, (150,150))
opening = pg.transform.scale(opening, (WIDTH, HEIGHT))

# initialise scores
X_SCORE = 0
O_SCORE = 0
    
def draw_board():
    pg.display.update()
    screen.fill(WHITE)
    draw_status()
    # drawing vertical lines
    pg.draw.line(screen,GRAY,(int(WIDTH/3),10),(int(WIDTH/3), int(HEIGHT-10)),10)
    pg.draw.line(screen,GRAY,(int(WIDTH/3*2),10),(int(WIDTH/3*2), int(HEIGHT-10)),10)
    # drawing horizontal lines
    pg.draw.line(screen,GRAY,(10,int(HEIGHT/3)),(int(WIDTH-10), int(HEIGHT/3)),10)
    pg.draw.line(screen,GRAY,(10,int(HEIGHT/3*2)),(int(WIDTH-10), int(HEIGHT/3*2)),10)
    
def show_score():
    score = "X  " + str(X_SCORE) + " : " + str(O_SCORE) + "  O"
    font = pg.font.Font(None, 30)
    text = font.render(score, 1, WHITE)
    text_rect = text.get_rect(center=(int(WIDTH/2), int(HEIGHT + 75)))
    screen.blit(text, text_rect)    
    
def draw_status():
    global DRAW, X_SCORE, O_SCORE
    if WINNER is None:
        message = XO.upper() + "'s Turn"
    else:
        if WINNER == 'x':
            X_SCORE += 1
        elif WINNER == 'o':
            O_SCORE += 1
        message = WINNER.upper() + " Won!"
    if DRAW:
        message = 'Game draw!'
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, WHITE)
    
    # copy the rendered message onto the board
    if XO == 'o':
        screen.fill (GREENGRAY, (0, 600, 700, 100))
        
    elif XO == 'x':
        screen.fill (GRAY, (0, 600, 700, 100))
        
    text_rect = text.get_rect(center=(int(WIDTH/2), int(HEIGHT + 25)))
    
    screen.blit(text, text_rect)
    show_score()
    
    pg.display.update()

def check_win():
    global BOARD, WINNER, DRAW
    # check for winning rows
    for row in range (0, 3):
        if ((BOARD [row][0] == BOARD[row][1] == BOARD[row][2]) and(BOARD[row][0] is not None)):
            # this row won
            WINNER = BOARD[row][0]
            if XO == 'x':
                pg.draw.line(screen, GREENGRAY, (0, int((row + 1) * HEIGHT/3 - HEIGHT/6)),\
                          (WIDTH, int((row + 1) * HEIGHT/3 - HEIGHT/6)), 8)
            elif XO == 'o':
                pg.draw.line(screen, GRAY, (0, int((row + 1) * HEIGHT/3 - HEIGHT/6)),\
                          (WIDTH, int((row + 1) * HEIGHT/3 - HEIGHT/6)), 8)
            break
            
    # check for winning columns
    for col in range (0, 3):
        if (BOARD[0][col] == BOARD[1][col] == BOARD[2][col]) and (BOARD[0][col] is not None):
            # this column won
            WINNER = BOARD[0][col]
            #draw winning line
            if XO == 'x':
                pg.draw.line (screen, GREENGRAY,(int((col + 1) * WIDTH/3 - WIDTH/6), 0),\
                          (int((col + 1) * WIDTH/3 - WIDTH/6), int(HEIGHT)), 8)
            elif XO == 'o':
                pg.draw.line (screen, GRAY,(int((col + 1) * WIDTH/3 - WIDTH/6), 0),\
                          (int((col + 1) * WIDTH/3 - WIDTH/6), HEIGHT), 8)
            break
            
    # check for diagonal WINNERs
    if (BOARD[0][0] == BOARD[1][1] == BOARD[2][2]) and (BOARD[0][0] is not None):
        # game won diagonally left to right
        WINNER = BOARD[0][0]
        if XO == 'x':
            pg.draw.line (screen, GREENGRAY, (50, 50), (550, 550), 8)
        elif XO == 'o':
            pg.draw.line (screen, GRAY, (50, 50), (550, 550), 8)
        
    if (BOARD[0][2] == BOARD[1][1] == BOARD[2][0]) and (BOARD[0][2] is not None):
        # game won diagonally right to left
        WINNER = BOARD[0][2]
        if XO == 'x':
            pg.draw.line (screen, GREENGRAY, (550, 50), (50, 550), 8)
        elif XO == 'o':
            pg.draw.line (screen, GRAY, (550, 50), (50, 550), 8)
        
    if(all([all(row) for row in BOARD]) and WINNER is None ):
        DRAW = True
        
    draw_status() 

def drawXO(row, col):
    global BOARD, XO
    if row == 1:
        posx = 30
    if row == 2:
        posx = int(WIDTH/3 + 30)
    if row == 3:
        posx = int(WIDTH/3*2 + 30)
    if col == 1:
        posy = 30
    if col == 2:
        posy = int(HEIGHT/3 + 30)
    if col == 3:
        posy = int(HEIGHT/3*2 + 30)
    BOARD[row-1][col-1] = XO
    if XO == 'x':
        screen.blit(x_img,(posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img,(posy, posx))
        XO = 'x'
    pg.display.update()
    
def userClick():
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()
    # get column of mouse click (1-3)
    if x < WIDTH/3:
        col = 1
    elif x < WIDTH/3*2:
        col = 2
    elif x < WIDTH:
        col = 3
    else:
        col = None
    # get row of mouse click (1-3)
    if y < HEIGHT/3:
        row = 1
    elif y < HEIGHT/3 * 2:
        row = 2
    elif y < HEIGHT:
        row = 3
    else:
        row = None
    # print(row,col)
    if (row and col and BOARD[row-1][col-1] is None):
        global XO
        # draw the x or o on screen
        drawXO(row, col)
        check_win()
        
def reset_game():
    global BOARD, WINNER, XO, DRAW, START
    time.sleep(3)
    
    # swap who starts
    if START == 'x':
        START = 'o'
        XO = 'o'
    else:
        START = 'x'
        XO = 'x'
        
    DRAW = False
    WINNER = None
    draw_board()
    BOARD = [[None]*3,[None]*3,[None]*3]

def button(msg,x,y,w,h,ic,ac, action = None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    # print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pg.draw.rect(screen, ac, (x,y,w,h))
        
        if click[0] == 1 and action != None:
            time.sleep(1)
            action()
            
    else:
        pg.draw.rect(screen, ic, (x,y,w,h))

    x_coord = int(x + (w/2))
    y_coord = int(y + (h/2))

    font = pg.font.Font(None, 30)
    text = font.render(msg, 1, WHITE)
    text_rect = text.get_rect(center=(x_coord, y_coord))
    screen.blit(text, text_rect)
    
def game_homepage():
    global X_SCORE, O_SCORE, BOARD
    
    # re initialise scores & board
    X_SCORE = 0
    O_SCORE = 0
    BOARD = [[None]*3,[None]*3,[None]*3]
    
    intro = True
    while intro:
        screen.fill(WHITE)
        screen.blit(opening,(0,0))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        button("Quit",100,620,150,60,GREENGRAY,LIGHTGREENGRAY, sys.exit)
        button("Play Game",350,620,150,60,GRAY,LIGHTGRAY, GameLoop)
        
        pg.display.update()            
    
def GameLoop():
    # init_global_vars()
    draw_board()
    
    # run the game loop forever
    while(True):
        if XO == 'o':
            button("Home", 450, 620, 80, 40, GRAY, LIGHTGRAY, game_homepage)

        elif XO == 'x':
            button("Home", 450, 620, 80, 40, GREENGRAY, LIGHTGREENGRAY, game_homepage)
    
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type is MOUSEBUTTONDOWN:
                # the user clicked; place an X or O
                userClick()
                
                if(WINNER or DRAW):
                    reset_game()
        pg.display.update()
        CLOCK.tick(fps)
        
def main():
    game_homepage()
    
if __name__ == "__main__":
    main()
