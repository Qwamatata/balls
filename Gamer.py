import pygame
import downloads
import settings

class Gamer:
    def __init__(self,game):
        self.picture = downloads.gamer
        self.hitbox = pygame.Rect([0,0],self.picture.get_size())
        self.game = game
    def draw(self,window):
        window.blit(self.picture,self.hitbox)
    def events(self):
        events  = pygame.event.get()
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.hitbox.centerx = mouse_pos[0]
        self.hitbox.centery = mouse_pos[1]
    def change_size(self):
        self.hitbox.w += 10
        self.hitbox.h += 10
        self.picture = pygame.transform.scale(self.picture,self.hitbox.size)