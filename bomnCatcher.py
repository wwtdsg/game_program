import pygame
from pygame.locals import *
import sys
import random


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Bomb Catching Game")
font1 = pygame.font.Font(None, 24)
pygame.mouse.set_visible(False)
white = 255, 255, 255
yellow = 230, 230, 50
black = 0, 0, 0

lives = 3
score = 0
game_over = True
mouse_x = mouse_y = 0
pos_x = 300
pos_y = 460
bomb_x = random.randint(0, 500)
bomb_y = -50
vel_y = 0.7
r = 200
g = 50
b = 50

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            move_x, move_y = event.rel
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False
                lives = 3
                score = 0

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0, 0, 100))

    if game_over:
        print_text(font1, 250, 200, "<click to play>")
    else:
        bomb_y += vel_y
        if bomb_y > 500:
            bomb_x = random.randint(0, 500)
            bomb_y = -50
            lives -= 1
            if lives == 0:
                vel_y = 0.7
                game_over = True

        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 120:
                score += 10
                vel_y += 0.2
                bomb_x = random.randint(0, 500)
                bomb_y = -50
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)

        pygame.draw.circle(screen, black, (bomb_x - 4, int(bomb_y - 4)), 30, 0)
        pygame.draw.circle(screen, yellow, (bomb_x, int(bomb_y)), 30, 0)

        pos_x = mouse_x
        if pos_x < 0:
            pos_x = 0
        elif pos_x > 500:
            pos_x = 500

        pygame.draw.rect(screen, black, (pos_x - 4, pos_y - 4, 120, 40), 0)
        pygame.draw.rect(screen, (r, g, b), (pos_x, pos_y, 120, 40), 0)

    print_text(font1, 0, 0, "LIVES: " + str(lives))
    print_text(font1, 300, 0, "SCORES: " + str(score))

    pygame.display.update()
