import pygame
from pygame.locals import *
import sys
import random


pygame.init()
screen = pygame.display.set_mode((600, 500))
font1 = pygame.font.Font(None, 24)
pygame.mouse.set_visible(False)
lives = 3
score = 0
game_over = True


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))


def collision(bomb, board):
    global flag
    if bomb.y > 500:
        bomb.x = random.randint(15, 485)
        bomb.y = -50
        global lives
        lives -= 1
        bomb.vel = 0.7
        bomb.color_change()
        flag = True
        if lives == 0:
            global game_over
            game_over = True
    elif bomb.y > board.y:
        if bomb.x > board.x and bomb.x < board.x + 120:
            global score
            score += 10
            bomb.accelerate(0.2)
            bomb.x = random.randint(15, 485)
            bomb.y = -50
            board.color_change()
            bomb.color_change()
            flag = True


class Bomb():
    def __init__(self):
        self.x = random.randint(15, 485)
        self.y = -50
        self.vel = 0.7
        self.color = 230, 230, 50

    def accelerate(self, dv):
        self.vel += dv

    def move(self):
        self.y += self.vel

    def color_change(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = r, g, b

    def creat(self, screen):
        pygame.draw.circle(screen, self.color, (self.x - 4, int(self.y - 4)), 30, 0)


class Board():
    def __init__(self):
        self.x = 300
        self.y = 460
        self.r = 200
        self.g = 40
        self.b = 40

    def color_change(self):
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def move(self, dy):
        self.y += dy

    def creat(self, screen):
        pygame.draw.rect(screen, (self.r, self.g, self.b), (self.x, self.y, 120, 40), 0)


board = Board()
bomb = Bomb()
mouse_x = 0
flag = True
while True:
    if flag:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        flag = False
    screen.fill((r, g, b))
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        elif event.type == MOUSEBUTTONUP:
            if game_over:
                game_over = False
                lives = 3
                score = 0

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    board.x = mouse_x
    if game_over:
        print_text(font1, 250, 200, "<CLICK TO PLAY>")
    else:
        bomb.move()
        collision(bomb, board)
        bomb.creat(screen)
    board.creat(screen)
    print_text(font1, 0, 0, "LIVES: " + str(lives))
    print_text(font1, 300, 0, "SCORE: " + str(score))
    pygame.display.update()
