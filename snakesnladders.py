# COMP 1405
# Hamid Ahmed
# 101256903
import random
import pygame

# DRAWING THE CHECKERBOARD
import pygame.time

#the two features for this game are sorry collisions where if the characters land on the same tile, they get sent back to square 9

height = 6
width = 7
squareSize = 90
drawing_window = pygame.display.set_mode(((width * squareSize) + 150, height * squareSize))
# added 150 pixels so there is space for dice values
drawing_window.fill((255, 255, 255))
# filled with white
red = (255, 50, 90)
black = (0, 0, 0)

# the below function creates a board, and it makes the code cleaner inside the while loop for the game
def board():
    current_colour = red
    # this uses a nested for loop to draw both the checkered tiles,and number the squares
    for i in range(7):
        for j in range(7):
            tileNumber = str((j * 7) + (i + 1))
            pygame.draw.rect(drawing_window, current_colour, (i * squareSize, j * squareSize, squareSize, squareSize))
            pygame.font.init()
            # initializing the font
            tileSpecs = pygame.font.SysFont('Times New Roman', 20, 1)
            # the font specifications
            tileFont = tileSpecs.render(tileNumber, False, (255, 255, 255))
            drawing_window.blit(tileFont, ((i * squareSize), (j * squareSize)))
            pygame.display.update()
            if current_colour == red:
                current_colour = black
            else:
                current_colour = red

                pygame.font.init()
                # initializing the font

# DICE

# this function does everything revolving aroud the dice, like rolling the dice values, getting the sum of the dice values, and displaying the text.
def dice():
    pygame.draw.rect(drawing_window, (255, 255, 255), (630, 0, 150, 540))
    diceOne = random.randint(1, 3)
    diceTwo = random.randint(1, 3)
    diceSUM = (diceOne + diceTwo)
    diceFont = pygame.font.SysFont('Times New Roman', 14)
    valueName = diceFont.render("Combined dice value:", False, (0, 0, 0))
    drawing_window.blit(valueName, (640, 40))
    gameFont = pygame.font.SysFont('Times New Roman', 20, 0)
    checkersName = gameFont.render(str(diceSUM), False, (0, 0, 0))
    drawing_window.blit(checkersName, (640, 55))
    gameFont = pygame.font.SysFont('Times New Roman', 20, 1)
    # the font specifications
    checkersName = gameFont.render("Board Game!", False, (0, 0, 0))
    # writing the text
    drawing_window.blit(checkersName, (640, 10))
    pygame.display.update()
    return diceSUM

#variables
turn = 0
yellowPlayerX = 1
yellowPlayerY = 0
greenPlayerX = 1
greenPlayerY = 0


while True:
    board()
    print(turn)
# modulus to determine each players turn, there is a turn counter implemented
    if turn % 2 == 1:
        #print(greenPlayerX)
        yellowPlayerX += dice()
        # dice returns dice sum
        #pygame.time.delay(100)
        if yellowPlayerX > 6:
            yellowPlayerY += 1
            yellowPlayerX -= 7
        yellowPlayer = pygame.draw.rect(drawing_window, (255, 255, 0),((yellowPlayerX * 90), (yellowPlayerY * 90), 20, 65))
        greenPlayer = pygame.draw.rect(drawing_window, (100, 255, 100),((greenPlayerX * 90) + 10, (greenPlayerY * 90), 20, 65))
        #pygame.time.delay(100)
        pygame.display.update()

    if turn % 2 == 0:
        greenPlayerX += dice()
        #pygame.time.delay(100)
        if greenPlayerX > 6:
            greenPlayerY += 1
            greenPlayerX -= 7
        yellowPlayer = pygame.draw.rect(drawing_window, (255, 255, 0), ((yellowPlayerX * 90), (yellowPlayerY * 90), 20, 65))
        #pygame.time.delay(100)
        greenPlayer = pygame.draw.rect(drawing_window, (100, 255, 100), ((greenPlayerX * 90) + 10, (greenPlayerY * 90), 20, 65))
        pygame.display.update()


    # SORRY COLLISIONS
    if yellowPlayerX and yellowPlayerY == greenPlayerX and greenPlayerY:
        yellowPlayerY = 1
        yellowPlayerX = 1

    if greenPlayerX and greenPlayerY == yellowPlayerX and yellowPlayerY:
        greenPlayerX = 1
        greenPlayerY = 1




    if (greenPlayerY >= 6):
        diceFont = pygame.font.SysFont('Times New Roman', 14)
        valueName = diceFont.render("Green player wins!", True, (0, 0, 0))
        drawing_window.blit(valueName, (600, 70))
        pygame.time.delay(1000)
        break
    elif (yellowPlayerY >= 6):
        diceFont = pygame.font.SysFont('Times New Roman', 14)
        valueName = diceFont.render("Yellow player wins!", True, (0, 0, 0))
        drawing_window.blit(valueName, (600, 70))
        break


    turn += 1
    pygame.time.delay(2000)





# this function allows the program to exit without crashing
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
