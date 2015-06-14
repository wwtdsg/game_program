import pygame
from pygame.locals import *
from datetime import datetime
import sys, math

pygame.init()
screen = pygame.display.set_mode((600, 500))
white = 255, 255, 255
pink = 255, 100, 100
yellow = 255, 255, 0
orange = 100, 180, 100

pos_x, pos_y = 300, 250
radius = 230
font = pygame.font.Font(None, 36)


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0, 0, 100))

    for n in range(1, 13):
        angle = math.radians(n * (360 / 12) - 90)
        x = math.cos(angle) * (radius - 20) - 10
        y = math.sin(angle) * (radius - 20) - 10
        print_text(font, pos_x + x, pos_y + y, str(n))
    pygame.draw.circle(screen, white, (pos_x, pos_y), radius, 6)

    today = datetime.today()
    hours = today.hour % 12
    minutes = today.minute
    seconds = today.second

    h_angle = (hours * 360 / 12.0 - 90) % 360 + minutes / 60.0 * 360 / 12
    h_angle = math.radians(h_angle)
    h_x = math.cos(h_angle) * (radius - 80)
    h_y = math.sin(h_angle) * (radius - 80)
    target = pos_x + h_x, pos_y + h_y
    pygame.draw.line(screen, pink, (pos_x, pos_y), target, 25)

    m_angle = (minutes * 360 / 60 - 90) % 360
    m_angle = math.radians(m_angle)
    m_x = math.cos(m_angle) * (radius - 60)
    m_y = math.sin(m_angle) * (radius - 60)
    target = pos_x + m_x, pos_y + m_y
    pygame.draw.line(screen, yellow, (pos_x, pos_y), target, 12)

    s_angle = (seconds * 360 / 60 - 90) % 360
    s_angle = math.radians(s_angle)
    s_x = math.cos(s_angle) * (radius - 40)
    s_y = math.sin(s_angle) * (radius - 40)
    target = pos_x + s_x, pos_y + s_y
    pygame.draw.line(screen, orange, (pos_x, pos_y), target, 6)

    pygame.draw.circle(screen, white, (pos_x, pos_y), 20, 0)
    pygame.display.update()
