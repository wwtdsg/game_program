#!-*- encoding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random


pygame.init()
screen = pygame.display.set_mode((600, 500))
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 34)
font3 = pygame.font.Font(None, 44)
pygame.mouse.set_visible(False)
lives = 3
score = 0
game_over = True


def compare(a, b):
    e1 = int(a.strip())
    e2 = int(b.strip())
    if e1 < e2:
        return -1
    elif e1 == e2:
        return 0
    else:
        return 1


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
        bomb.vel = 1.7
        if lives == 0:
            global game_over
            game_over = True
    elif bomb.y > board.y:
        if bomb.x > board.x - 15 and bomb.x < board.x + 120:
            global score
            score += 10
            bomb.accelerate(0.2)
            flag = True
            bomb.x = random.randint(15, 485)
            bomb.y = -50
            board.color_change()
            bomb.color_change()
            flag = True


class Bomb():
    def __init__(self):
        self.x = random.randint(15, 485)
        self.y = -50
        self.vel = 1.7
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

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
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def color_change(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = r, g, b

    def move(self, dy):
        self.y += dy

    def creat(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 120, 40), 0)


board = Board()
bomb = Bomb()
mouse_x = 0
flag = True
game_start = True
record_posible = True
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
            game_start = False
            record_posible = True
            if game_over:
                game_over = False
                lives = 3
                score = 0

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    board.x = mouse_x

    if game_start:
        print_text(font1, 250, 250, "<CLICK TO PLAY>")
    elif game_over:
        # 文件处理，记录保存
        if record_posible:
            record_posible = False
            ran = 0
            try:
                f = open(r'bomb_record.txt')
            except:
                f = open(r'bomb_record.txt', 'w')
                f.close()
                f = open(r'bomb_record.txt')
            records = f.readlines()
            new_records = records[:]
            f.close()
            new_records.append(str(score) + '\n')
            new_records.sort(cmp=compare, reverse=True)
            ran = new_records.index(str(score) + '\n')
            f = open(r'bomb_record.txt', 'w')
            for line in new_records:
                f.write(line)
            f.close()
        print_text(font1, 40, 250, "YOU SCORED %d POINTS, RANGE %d" % (score, ran + 1))
        if ran == 0:
            print_text(font3, 40, 100, "Wanderful!")
            print_text(font3, 40, 150, "You just made a new record!")
        else:
            print_text(font2, 40, 200, "GAME OVER!")
        print_text(font1, 40, 300, "<CLICK TO TRY AGAIN>")

    else:
        bomb.move()
        collision(bomb, board)
        bomb.creat(screen)
    board.creat(screen)
    print_text(font1, 0, 0, "LIVES: " + str(lives))
    print_text(font1, 300, 0, "SCORE: " + str(score))
    pygame.display.update()
