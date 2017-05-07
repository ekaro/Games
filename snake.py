# Snake Game

import pygame, sys, random, time

check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

# Play Surface
X = 1920
Y = 1080
playSurface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Snake Game')
time.sleep(5)

# Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

# FPS controller
fpsController = pygame.time.Clock()

# Variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, X/10) * 10, random.randrange(1, Y/10) * 10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0

myFont = pygame.font.SysFont('monaco', 72)

# Game over fuction
def gameOver():
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (X/2, 20)
    playSurface.blit(GOsurf, GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()  # pygame exit
    sys.exit()  # console

def showScore(choice=1):
    scoreFont = pygame.font.SysFont('monaco', 24)
    Ssurf = myFont.render('Score: ' + str(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (100, 10)
    else:
        Srect.midtop = (X/2, Y/2)
    playSurface.blit(Ssurf, Srect)

# time.sleep(10)

# Main logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

                # validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    if foodSpawn == False:
        foodPos = [random.randrange(1, X/10) * 10, random.randrange(1, Y/10) * 10]
    foodSpawn = True

    playSurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0] > X-10 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > Y-10 or snakePos[1] < 0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip()  # update
    fpsController.tick(25)