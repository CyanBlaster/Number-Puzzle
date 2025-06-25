import sys
import pygame
import datetime
import math
import pygame.freetype

pygame.init()
GAME_FONT = pygame.freetype.Font("DayDream.ttf", 24)


def ZeroField(n):
    return [[0] * n for i in range(n)]
def main():
    array = [[0, 1, 2, 3, 4], [6, 5, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
    width = 501
    height = 501
    screen = pygame.display.set_mode((width, height))
    running = True
    xIdx = 2
    yIdx = 2
    board = ZeroField(20)
    while running:
        pygame.display.flip()
        screen.fill((0, 0, 0))
        for i in range(0, 5):
            pygame.draw.line(screen, (0, 0, 255), (i * 500/5, 0), (i * 500/5, 500))
            pygame.draw.line(screen, (0, 0, 255), (0, i * 500/5), (500, i * 500/5))
        pygame.draw.rect(screen, (255, 255, 255), (xIdx * 100 + 1, yIdx * 100 + 1, 99, 99))

        for x in range(5):
            for y in range(5):
                if(array[x][y] != 0):
                    text_surface, rect = GAME_FONT.render(str(array[x][y]), (255, 0, 0))
                    screen.blit(text_surface, (y * 100 + 50 - rect.width/2, x * 100 + 50 - rect.height/2))

        if (array == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]):
            print("win")
            running = False


        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                    xIdx -= 1
                    if(xIdx == -1):
                        xIdx = 0
                elif events.key == pygame.K_RIGHT:
                    xIdx += 1
                    if(xIdx == 5):
                        xIdx = 4
                elif events.key == pygame.K_UP:
                    yIdx -= 1
                    if(yIdx == -1):
                        yIdx = 0
                elif events.key == pygame.K_DOWN:
                    yIdx += 1
                    if(yIdx == 5):
                        yIdx = 4
                elif events.key == pygame.K_SPACE:
                    if (xIdx >= 1 and array[yIdx][xIdx - 1] == 0):
                        s = array[yIdx][xIdx]
                        array[yIdx][xIdx] = array[yIdx][xIdx - 1]
                        array[yIdx][xIdx - 1] = s
                        print(array[yIdx][xIdx], " ", array[yIdx][xIdx - 1])
                    elif (xIdx < 4 and array[yIdx][xIdx + 1] == 0):
                        s = array[yIdx][xIdx]
                        array[yIdx][xIdx] = array[yIdx][xIdx + 1]
                        array[yIdx][xIdx + 1] = s
                        print(array[yIdx][xIdx], " ", array[yIdx][xIdx + 1])
                    elif (yIdx < 4 and array[yIdx + 1][xIdx] == 0):
                        s = array[yIdx][xIdx]
                        array[yIdx][xIdx] = array[yIdx + 1][xIdx]
                        array[yIdx + 1][xIdx] = s
                        print(array[yIdx][xIdx], " ", array[yIdx + 1][xIdx])
                    elif (yIdx >= 1 and array[yIdx - 1][xIdx] == 0):
                        s = array[yIdx][xIdx]
                        array[yIdx][xIdx] = array[yIdx - 1][xIdx]
                        array[yIdx - 1][xIdx] = s
                        print(array[yIdx][xIdx], " ", array[yIdx - 1][xIdx])

main()