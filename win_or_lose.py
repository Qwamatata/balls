import pygame
import downloads
class end:
    def __init__(self, game):
        self.game = game
        if self.game.condition == 'win':
            self.picture = downloads.win
            self.hitbox = pygame.Rect([0, 0], self.picture.get_size())
        elif self.game.condition == 'lose':
            self.picture = downloads.lose
            self.hitbox = pygame.Rect([0, 0], self.picture.get_size())



    def draw(self):
        self.game.window.blit(self.picture,self.hitbox)
        if self.game.fp == 20:
            self.game.condition = 'win'

