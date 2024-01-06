import pygame
from pygame.locals import *
import numpy as np
import sys
import time

pygame.init()

SCREEN_W = 800
SCREEN_H = 800

screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
yellow = ((255,255,0))
font = pygame.font.Font('freesansbold.ttf', 64)

screen.fill(black)

pygame.display.set_caption('Liquid Classification')

button_text = font.render('Classify Liquid', True, black, green)
button_textframe = button_text.get_rect()
button_textframe.center = (SCREEN_W // 2, SCREEN_H // 2 - SCREEN_H/4)

return_text = font.render('No Liquid Sampled', True, black, white)
return_textframe = return_text.get_rect()
return_textframe.center = (SCREEN_W // 2, SCREEN_H // 2 + SCREEN_H/4)

not_pressed = 1

while True:
    
    clock.tick(60)

###############################Check for quitting##########################################
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if (160 <= mouse[0] <= 640) and (165 <= mouse[1] <= 230):
                not_pressed = 0
                
        
    screen.fill(white)
    if not (not_pressed):
        button_text = font.render('Classify Liquid', True, black, yellow)
    screen.blit(return_text, return_textframe)
    screen.blit(button_text, button_textframe)
    pygame.display.update()

    if not (not_pressed):
        print('Execute program')
        time.sleep(2)
        button_text = font.render('Classify Liquid', True, black, green)
        not_pressed = 1
