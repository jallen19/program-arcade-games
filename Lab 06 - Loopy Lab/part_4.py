#!/usr/bin/env python3
# chap6.py
# James Allen
#11/13/2017

import pygame
pygame.init()

RED = (255, 0, 0)
BLACK = (0, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

pygame.display.set_caption('Sea of Red')

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(BLACK)
    
    for y in range(0, 700, 10):
        for x in range(0, 700, 10):
            pygame.draw.rect(screen, RED, (x,y,5,5), 0)
            
            
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()