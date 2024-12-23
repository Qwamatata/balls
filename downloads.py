import pygame
import settings

pygame.init()

# DOWNLOADS
back = pygame.image.load('back.jpg')
menu = pygame.image.load('menu.jpg')
gamer = pygame.image.load('gamer.png')
ball = pygame.image.load('ball.png')
button = pygame.image.load('button.png')
win = pygame.image.load('win.jpg')
lose = pygame.image.load('lose.jpg')
live_not = pygame.mixer.Sound('live.mp3')
back_mus = pygame.mixer.Sound('music.mp3')
start = pygame.mixer.Sound('start.mp3')

# TRANSFORM
back = pygame.transform.scale(back, settings.SIZE)
menu = pygame.transform.scale(menu, settings.SIZE)
gamer = pygame.transform.scale(gamer, [100, 100])
win = pygame.transform.scale(win, settings.SIZE)
lose = pygame.transform.scale(lose, settings.SIZE)
