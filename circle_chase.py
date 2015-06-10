import sys
import pygame
import math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("circle_chase")
pygame.key.set_repeat(10)
screen.fill((0, 0, 200))


class atom:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.color = 255, 255, 0
        self.redius = 5
        self.width = 5

    def move(self, x, y):
        self.x += x
        self.y += y


a = atom()
pygame.draw.circle(screen, a.color, (a.x, a.y), a.redius, a.width)
pygame.display.update()
angle = 0
flag = 1
while 1:
    x = 100 * math.cos(angle) + 300
    y = 100 * math.sin(angle) + 250
    angle += 0.005
    pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 16, 16)
    pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 10, 10)
    pygame.display.update()
    # elif event.type is pygame.K_DOWN.set_repeat(10):
    for event in pygame.event.get():
        if event.type is QUIT:
            sys.exit()
        elif event.type is KEYDOWN:
            if event.key == pygame.K_LEFT:
                a.move(-2, 0)
                pygame.draw.circle(screen, (100, 0, 100), (a.x, a.y), a.redius + 3, a.width + 3)
                pygame.draw.circle(screen, a.color, (a.x, a.y), a.redius, a.width)
            elif event.key == pygame.K_RIGHT:
                a.move(2, 0)
                pygame.draw.circle(screen, (100, 0, 100), (a.x, a.y), a.redius + 3, a.width + 3)
                pygame.draw.circle(screen, a.color, (a.x, a.y), a.redius, a.width)
            elif event.key == pygame.K_DOWN:
                a.move(0, 2)
                pygame.draw.circle(screen, (100, 0, 100), (a.x, a.y), a.redius + 3, a.width + 3)
                pygame.draw.circle(screen, a.color, (a.x, a.y), a.redius, a.width)
            elif event.key == pygame.K_UP:
                a.move(0, -2)
                pygame.draw.circle(screen, (100, 0, 100), (a.x, a.y), a.redius + 3, a.width + 3)
                pygame.draw.circle(screen, a.color, (a.x, a.y), a.redius, a.width)
