import pygame
import time
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 155, 0)

lead_x = 400
lead_y = 300

lead_x_change = 0
lead_y_change = 0

block_size = 10
snakeLength = 1

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake')

font = pygame.font.SysFont(None, 25)

clock = pygame.time.Clock()

snakeList = []

def score(num):
    text = font.render("Score : " + str(num), True, BLACK)
    gameDisplay.blit(text, [10, 10])

def snake(snakeList):
    for li in snakeList:
        pygame.draw.rect(gameDisplay, BLACK, [li[0], li[1], block_size, block_size])

gameExit = False
gameDisplay.fill(WHITE)

randomAppleX = round(random.randrange(0 + 10, 800 - 10) / 10.0) * 10.0
randomAppleY = round(random.randrange(0 + 10, 600 - 10) / 10.0) * 10.0

while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0

    if lead_x >= 800 or lead_x <= 0 or lead_y >= 600 or lead_y <= 0:
        gameExit = True

    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(WHITE)

    pygame.draw.rect(gameDisplay, RED, [randomAppleX, randomAppleY, block_size, block_size])

    snakeHead = []
    snakeHead.append(lead_x)
    snakeHead.append(lead_y)

    if len(snakeList) >= snakeLength:
        del snakeList[0]

    for x in snakeList[:-1]:
        if snakeHead == x:
            gameExit = True

    snakeList.append(snakeHead)

    snake(snakeList)
    score(snakeLength - 1)
    pygame.display.update()

    if lead_x == randomAppleX and lead_y == randomAppleY:
        randomAppleX = round(random.randrange(0 + 10, 800 - 10) / 10.0) * 10.0
        randomAppleY = round(random.randrange(0 + 10, 600 - 10) / 10.0) * 10.0
        snakeLength += 1

    clock.tick(30)

pygame.quit()
