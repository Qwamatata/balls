import pygame
import random
import downloads
import settings


class Balls():
    def __init__(self, game):
        self.game = game
        self.picture = downloads.ball
        self.rand = random.randint(self.game.gamer.hitbox.w-50,self.game.gamer.hitbox.w + 100)
        self.picture = pygame.transform.scale(self.picture, (self.rand,self.rand))
        self.num = random.randint(1,4)
        if self.num == 1:
            self.hitbox = pygame.Rect([0,random.randint(0,settings.HEIGHT)], self.picture.get_size())
            self.speed_x = random.randint(1,3)
            self.speed_y = random.randint(-3,3)
        elif self.num == 2:
            self.hitbox = pygame.Rect([random.randint(0,settings.WEIGHT),0],self.picture.get_size())
            self.speed_x = random.randint(-3,3)
            self.speed_y = random.randint(1,3)
        elif self.num == 3 :
            self.hitbox = pygame.Rect([settings.WEIGHT,random.randint(0,settings.HEIGHT)],self.picture.get_size())
            self.speed_x = random.randint(-3,-1)
            self.speed_y = random.randint(-3,3)
        elif self.num == 4 :
            self.hitbox = pygame.Rect([random.randint(0,settings.HEIGHT),settings.HEIGHT],self.picture.get_size())
            self.speed_x = random.randint(-3,3)
            self.speed_y = random.randint(-3,-1)


    def update(self):
        self.hitbox.x += self.speed_x
        self.hitbox.y += self.speed_y

    def draw(self):
        self.game.window.blit(self.picture,self.hitbox)