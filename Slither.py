import pygame
from random import randrange
pygame.init()
clock = pygame.time.Clock()
display_width = 800
display_height = 600
red = (255, 0, 0)
green = (0, 100, 0)
white = (255, 255, 255)
black = (0, 0, 0)
yellow=(255,255,0)
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")
'''icon=pygame.image.load('apple.png')
pygame.display.set_icon(icon)#to set icon to your window'''
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 75)
img=pygame.image.load("snakeHead.png")
img2=pygame.image.load('apple.png')
direction="right"

def pause():
    paused=True
    while(paused):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        win.fill(white)
        message_to_screen("Paused!!",red,-100,size="large")
        message_to_screen("Press c to continue or q to quit",black,25)
        pygame.display.update()
        clock.tick(5)
def text_objects(text,color,size):
    if size=="small":
        textSurface=smallfont.render(text,True,color)
    elif size=="medium":
        textSurface=medfont.render(text,True,color)
    if size=="large":
        textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()

def message_to_screen(msg, color,y_displace=0,size="small"):
    textSurf,textRect=text_objects(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+y_displace
    win.blit(textSurf,textRect)

def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        win.fill(white)
        message_to_screen("Welcome to Slither",green,-100,size="large")
        message_to_screen("The objective of the game is to eat apples",black,-30)
        message_to_screen("The more apples you eat the longer you get", black, 10)
        message_to_screen("If you run into yourself or the edges you die!", black, 50)
        message_to_screen("Press c to play, p to pause or q to quit.", black, 180)
        pygame.display.update()
        clock.tick(15)

def score(score):
    text=smallfont.render("Your Score: "+str(score),True,white)
    win.blit(text,[0,0])

def randappleGen(appleSize):
    randappleX = round(randrange(0, display_width - appleSize - 10) / 10.0) * 10.0
    randappleY = round(randrange(0, display_height - appleSize - 10) / 10.0) * 10.0
    return randappleX,randappleY

def snake(block_size, snakeList):
    if direction=="right":
        head=pygame.transform.rotate(img,270)
    if direction=="left":
        head=pygame.transform.rotate(img,90)
    if direction=="up":
        head=img
    if direction=="down":
        head=pygame.transform.rotate(img,180)
    win.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(win, green, (XnY[0], XnY[1], block_size, block_size))

def gameLoop():
    global direction
    direction='right'
    block_size = 20
    appleSize = 20
    lead_x = 250
    lead_y = 250
    lead_x_change = 10
    lead_y_change = 0
    run = True
    FPS = 15
    randappleX,randappleY=randappleGen(appleSize)
    snakeList = []
    snakeLength = 1
    gameOver = False
    vel=10
    while (run):
        while gameOver == True:
            win.fill(white)
            message_to_screen("Game Over!" , red,-50,size="large")
            message_to_screen(f"press c to play or q to quit ",black,50,size="medium")
            message_to_screen("Your Score: "+str(snakeLength-1),black,120)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_q:
                        run = False
                        gameOver = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -vel
                    lead_y_change = 0
                    direction="left"
                if event.key == pygame.K_RIGHT:
                    lead_x_change = vel
                    lead_y_change = 0
                    direction = "right"
                if event.key == pygame.K_UP:
                    lead_y_change = -vel
                    lead_x_change = 0
                    direction = "up"
                if event.key == pygame.K_DOWN:
                    lead_y_change = vel
                    lead_x_change = 0
                    direction = "down"
                if event.key==pygame.K_p:
                    pause()
        lead_x += lead_x_change
        lead_y += lead_y_change
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if lead_x < 0 or lead_x >= display_width - block_size or lead_y < 0 or lead_y >= display_height - block_size:
            gameOver = True
        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        if lead_x >= randappleX and lead_x <= randappleX + appleSize or lead_x + block_size > randappleX and lead_x + block_size < randappleX + appleSize:
            if lead_y >= randappleY and lead_y <= randappleY + appleSize or lead_y + block_size > randappleY and lead_y + block_size < randappleY + appleSize:
                randappleX,randappleY=randappleGen(appleSize)
                snakeLength += 1
        win.fill(black)
        #pygame.draw.rect(win, red, (randappleX, randappleY, appleSize, appleSize))
        win.blit(img2,(randappleX,randappleY))
        snake(block_size, snakeList)
        score(snakeLength - 1)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
game_intro()
gameLoop()



