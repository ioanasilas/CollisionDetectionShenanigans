import pygame
import pygame.gfxdraw
import sys
import math
import random
import time
from random_testing import circleCircleRandom, polygonPolygonRandom, circleLineRandom, aabbRandom, lineLineRandom
from no_overlap_testing import circleCircleNonOverlap, aabbNoOverlap
from shared_data import shapes

WHITE = (255, 255, 255)
RED = (200, 100, 100)
GREEN = (100, 200, 150)
GREY = (25, 25, 25)


pygame.init()
screen = pygame.display.set_mode((1024, 618))
pygame.display.set_caption("Collision Detection Tests")

# circleCircleRandom()
# aabbRandom()
# lineLineRandom()
# circleLineRandom()
# polygonPolygonRandom()

avgTime = 0.0
runs = 0.0
outline = 1
running = True
while running:
    screen.fill(GREY)
    shapes.clear()
    # polygonPolygonRandom()
    # circleLineRandom()
    # lineLineRandom()
    # aabbRandom()
    # circleCircleRandom()

    # circleCircleNonOverlap()
    aabbNoOverlap()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and (48 <= event.key <= 57):
            outline = int(chr(event.key))
    
    # timing just actual sorting, you're cool yousef \o/
    startTime = time.time()
    for i in range(len(shapes)):
        if shapes[i].intersecting == False:
            for v in range(len(shapes)):
                if i == v:
                    continue
                
                if (shapes[i].intersects(shapes[v])):
                    shapes[i].intersecting = True
                    shapes[v].intersecting = True
                    intersects = True
                    break
        
        if shapes[i].intersecting == True:
            shapes[i].draw(screen, RED, outline)
        else:
            shapes[i].draw(screen, GREEN, outline)
    
    timeTaken = (time.time() - startTime)
    runs += 1
    avgTime = avgTime + (timeTaken - avgTime) / runs
    print("Time Taken: ", timeTaken)
    print("Current Average: ", avgTime)
    print()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()